import xbrl
import xlsxwriter

class ExcelDump(object):

    def __init__(self, xbrl_obj):
        self.xbrl_obj = xbrl_obj

    def dump(self, workbook_name):

        workbook = xlsxwriter.Workbook(workbook_name)
        worksheet = workbook.add_worksheet()

        for idx, val in enumerate(self.xbrl_obj.__dict__.items()):
            worksheet.write(idx, 0, val[0].replace("_", " "))
            worksheet.write(idx, 1, val[1])
        workbook.close()
