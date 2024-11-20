from os import path as os_path
from immutableType import Tuple_, Str_

from .ERRORS import PathError
from .color import Style
set_style = Style()

class Compressor:

    def __init__(self):
        """
        Init Compressor class.
        """
        self.files: list[str] = []
        self.folders: list[str] = []
        self.destination: str = ''

    def start_compressor(self, *paths, destination: str='') -> str:
        """

        :param paths: All paths to compress (files or directories)
        :param destination: The path to the compressed file destination
        :return: The compressed file path
        """
        destination = Str_(destination)
        paths = Tuple_(paths)

        self.__split_paths(paths, destination=destination.str_)



    def __split_paths(self, paths, destination:str)->None:
        """
        Check if all paths exists
        :param paths: all paths
        :param destination: The destination path for the compressed file
        :return: None
        """
        files = []
        folders = []

        for path in paths:

            if not os_path.exists(path):  # si le chemin d'accès n'existe pas
                raise PathError(
                    set_style.color_arg(path, set_style.LIGHT_GREEN))  # on renvoie une erreur avec le chemin en vert

            if os_path.isdir(path): # si le chemin mène vers un dossier
                folders.append(path)

            if os_path.isfile(path): # si le chemin mène vers un fichier
                files.append(path)

        self.destination = destination
        self.folders = folders
        self.files = files
