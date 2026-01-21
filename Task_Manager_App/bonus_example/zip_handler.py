import zipfile 
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path=pathlib.Path(dest_dir,"compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)
            
def extract_archive(archivePath, dest_dir):
    with zipfile.ZipFile(archivePath, 'r') as archive:
        archive.extractall(dest_dir)
            
if __name__ == "__main__":
    extract_archive(
        pathlib.Path("bonus_example") / "dest" / "compressed.zip",
        pathlib.Path("bonus_example")/"extract"
    )

    #make_archive(filepaths=["yesterdays_bonus13.py"], dest_dir= "dest")
    #extract_archive("\\bonus_example\\dest\\compressed.zip","extract" )
    
    