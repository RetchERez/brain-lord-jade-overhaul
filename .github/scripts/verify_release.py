"""Check the exact public player release and its native-size media."""
from pathlib import Path
import hashlib,json,re,struct,zipfile,zlib

root=Path(__file__).resolve().parents[2]
manifest=json.loads((root/'release-manifest.json').read_text())
for name,digest in manifest['files_sha256'].items():
    path=root/name
    assert path.is_file(),name
    assert hashlib.sha256(path.read_bytes()).hexdigest()==digest,name
    if path.suffix=='.gif':
        data=path.read_bytes();assert data[:6] in (b'GIF87a',b'GIF89a')
        assert struct.unpack('<HH',data[6:10])[0]==600,name
    if path.suffix=='.png':
        data=path.read_bytes();assert data[:8]==b'\x89PNG\r\n\x1a\n'
        assert struct.unpack('>II',data[16:24])==(256,224),name
for path in root.rglob('*'):
    if '.git' in path.parts or not path.is_file():continue
    assert path.suffix.lower() not in {'.sfc','.smc','.srm','.sav','.state','.bst'},path
    assert not any(part in {'.local','.superpowers','__pycache__'} for part in path.parts),path
patch=(root/manifest['patch']).read_bytes()
assert patch[:4]==b'BPS1'
assert zlib.crc32(patch[:-4])&0xffffffff==int.from_bytes(patch[-4:],'little')
assert f"{int.from_bytes(patch[-12:-8],'little'):08X}"==manifest['source']['crc32']
assert f"{int.from_bytes(patch[-8:-4],'little'):08X}"==manifest['target']['crc32']
with zipfile.ZipFile(root/manifest['archive']) as archive:
    assert archive.namelist()==[Path(manifest['patch']).name,'readme.txt']
    assert archive.testzip() is None
    assert archive.read(Path(manifest['patch']).name)==patch
    assert archive.read('readme.txt')==(root/'readme.txt').read_bytes()
with zipfile.ZipFile(root/manifest['screenshots_archive']) as archive:
    images=sorted((root/'media/screenshots').glob('*.png'))
    assert sorted(archive.namelist())==[p.name for p in images]
    assert all(archive.read(p.name)==p.read_bytes() for p in images)
for line in (root/'SHA256SUMS.txt').read_text().splitlines():
    digest,name=line.split()
    assert hashlib.sha256((root/'downloads'/name).read_bytes()).hexdigest()==digest,name
text=(root/'readme.txt').read_text()
assert manifest['target']['sha256'] in text
assert not any('.' in line for line in text.splitlines() if line.lstrip().startswith('- '))
for path in (root/'forum-posts').glob('*.bbcode.txt'):
    post=path.read_text();assert 'height=' not in post.lower()
    images=re.findall(r'\[img\](.*?)\[/img\]',post,re.I)
    assert len(images)==7,(path,len(images))
    for url in images:
        prefix=manifest['raw_base']+'/'
        assert url.startswith(prefix),url
        assert (root/url.removeprefix(prefix)).is_file(),url
print('PASS: exact BPS and ZIP, checksums, 4 GIFs at 600px, 9 screenshots at 256x224, forum assets and public-file exclusions')
