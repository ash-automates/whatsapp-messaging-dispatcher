#!/usr/bin/python3
import openpyxl, os, pywhatkit, pyautogui, time

wb = openpyxl.load_workbook("contact_list.xlsx")
numbers_sheet = wb.active

archived_nums = []
numbers_to_contact = []
