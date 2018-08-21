#!/usr/bin/python3
# -*- coding:utf-8 -*-
import xlrd
import xlwt
import xlutils.copy


class WriteExcel():

    def __init__(self, wb_name):
        self.wb = xlwt.Workbook(wb_name)
        self.file_name = wb_name
        sheet = self.wb.add_sheet('sheet1')
        sheet.write(0, 0, '商品及关键字')
        sheet.write(0, 1, '商家')
        sheet.write(0, 2, '价格')
        sheet.write(0, 3, '购买人数')
        sheet.write(0, 4, '商家所在地')
        sheet.write(0, 5, '商品链接')
        self.wb.save('./{}.xls'.format(self.file_name))
        self.i = 1

    def write(self, results):
        rb = xlrd.open_workbook('./{}.xls'.format(self.file_name))
        wb = xlutils.copy.copy(rb)
        sheet = wb.get_sheet(0)
        for key, value in results.items():
            if key == 'title':
                sheet.write(self.i, 0, value)
            elif key == 'shop':
                sheet.write(self.i, 1, value)
            elif key == 'price':
                sheet.write(self.i, 2, value)
            elif key == 'deal':
                sheet.write(self.i, 3, value)
            elif key == 'location':
                sheet.write(self.i, 4, value)
            elif key == 'url':
                sheet.write(self.i, 5, value)
        self.i += 1
        wb.save('./{}.xls'.format(self.file_name))
