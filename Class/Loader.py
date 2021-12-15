import os

class Loader():
    """Class that allow to operate with a source file
    """
    def __init__(self, path: str) -> None:
        """Istanciate the loader with the path of the file to be analized
        
        Parameters
        ----------
        path : str
            The path of the file
        
        """
        if len(path) < 3:
            raise ValueError("Path should not be less than 3 character!") 
        if not os.path.exists(path):
            raise FileNotFoundError("The given path doesn't exist")
        if not os.path.isfile(path):
            raise NameError("The given path isn't a file!")
        
        print("Acquiring the path file..")
        self.path = path
        print("Ok.")
    
    def load(self) -> str:
        """Method that allow to read the data inside the loaded file

        Returns
        -------
        str
            A string containing all the lines inside the file

        Raises
        ------
        ex
            An exception when the file is opened or when the file object is read
        """
        print("Starting reading..")
        _temp_data : str = ""
        try:
            with open(self.path,"r") as file:
                _temp_data = file.read()
        except Exception as ex:
            print(ex.with_traceback)
            raise ex
        print("Reading done..")
        return _temp_data
             
        