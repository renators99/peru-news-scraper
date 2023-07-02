from utils.scrapers.comercio.utils.sitemap import get_sections
class Comercio():
    """
    This class is designed to handle the ETL 
    (Extract, Transform, Load) process.
    """
    def __init__(self, step = None):
        """
        Initialize a new instance of the CodigoCPP class.

        :param step: The ETL process step to execute, 
        which can be 'extract', 'transform', 'load', or 'all'.
        """
        self.load_type = step
    
    def extract(self):
        """
        Executes the extraction step of the ETL process, 
        extracting files from SPIJ.
        """
        get_sections()
    
    def transform(self):
        """
        Executes the transformation step of the ETL process, 
        converting files into JSON format.
        """
        pass

    def load(self):
        """
        Executes the load step of the ETL process, 
        initializing Pinecone and OpenAI, and uploading data 
        to Pinecone.
        """
        pass

    def all(self):
        """
        Executes all steps of the ETL process 
        (extract, transform, load) in sequence.
        """
        pass
        
    def run(self):
        """
        Runs the ETL process step specified in init
        """
        getattr(self, self.load_type)()