"""Class to create HTML files"""

#import string

class WriteHtml(object):
    """
    holds all the formatting elements to create the file
    - header
    - footer
    - individual plots
    - tables
    """
    #_file_handle = 0

    def __init__(self, thefilename):
        """
        initialization: creates new file with header.
        Overwrites if already existing
        """
        self.file_handle = open(thefilename, "w")

    def write_header(self, title):
        """
        Write the header stuff
        """
        self.file_handle.write('<!DOCTYPE html>\n'
                               + '<html>\n'
                               + '\n'
                               + '<head>\n'
                               + '  <title>' + title + '</title>\n'
                               + '</head>\n'
                               + '\n'
                               + '<body>\n')

    def write_footer(self):
        """
        Close the html file properly
        """
        self.file_handle.write('</body>\n \n </html>\n')

    def add_plot(self, plotstring):
        """
        create entry for one plot based on the return value
        of the plotting function
        """
        self.file_handle.write('to be implemented' + plotstring + '\n')

    def add_table(self, tablecontent):
        """
        create table in html style
        """
        self.file_handle.write('to be implemented' + tablecontent + '\n')
