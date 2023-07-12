import os

class ProjectBase:
    @staticmethod
    def get_project_location():
        current_file = os.path.abspath(__file__)
        project_location = os.path.dirname(current_file)
        return project_location

class FolderController(ProjectBase):
    def __init__(self) -> None:
        self.images_location = None

    @staticmethod
    def create_folder(path):
        if not os.path.exists(path):
            os.makedirs(path)

    def create_images_folder(self):
        project_location = self.get_project_location()
        self.images_location = os.path.join(project_location, 'images')
        self.create_folder(self.images_location)
    
    def get_images_path(self):
        return self.images_location