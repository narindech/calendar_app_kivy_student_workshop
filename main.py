from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty, NumericProperty
from kivy.properties import StringProperty
import zeller as zl
from datetime import date


class SplashScreen(Screen):
    pass

class MainScreen(Screen):

    month_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    count = 0
    count_str = StringProperty(str(count))
    count_year = 0
    kv_year = StringProperty(str(count_year))

    def show_today_date(self):
        this_day = date.today()
        print(this_day) # str 2022-12-17

        # "2022-12-17" -> string 
        # day = 17
        # month = 12
        # year = 2022
        # split() -> python string operation
        datetime_split = str(this_day).split("-")
        print("show me ----> ", datetime_split)
        day = int(datetime_split[2])
        month = int(datetime_split[1]) # 1 -> January
        year = int(datetime_split[0])
        result_from_zl = zl.Zellercongruence(day, month, year)
        print("result from zl --> ", result_from_zl)

        month_name = self.month_list[month - 1]
        self.count_str = str(month_name)

        self.count_year = year
        self.kv_year = str(self.count_year)
        
        self.count = month - 1
        self.modify_calendar()
        self.color_date()


    def next_button_pressed(self):
        # ถ้า self.count มีค่าเป็น 11 ทันทีที่กดปุ่ม next ให้มัน reset ค่าเป็น 0
        self.count += 1 # 11 -> 12 
        if self.count == 12:
            # เพิ่มจำนวนปีถัดไป
            self.count = 0
            self.count_year += 1       
        self.kv_year = str(self.count_year)
        month_name = self.month_list[self.count] # Apr
        self.count_str = str(month_name)
        # 1, month, 2023 --> what day of week?
        first_day = zl.Zellercongruence(1, self.count + 1, self.count_year)
        print("next_button_pressed is called.", first_day)
        self.modify_calendar()
        self.color_date()

    def back_button_pressed(self):
        self.count -= 1
        if self.count == -1:
            # ลดจำนวนปีก่อนหน้า
            self.count = 11
            self.count_year -= 1
        self.kv_year = str(self.count_year)
        month_name = self.month_list[self.count] # Apr
        self.count_str = str(month_name)
        print("back_button_pressed is called.")
        self.modify_calendar()
        self.color_date()

    def modify_calendar(self):
        # ทำหน้าที่ในการเปลี่ยนแปลง วันที่ ตามเดือนที่เปลี่ยนแปลงไป
        print("modify_calendar is called.")

        month_number = self.count + 1
        _31_day_month = [1, 3, 5, 7, 8, 10, 12]
        _30_day_month = [4, 6, 9, 11]
        _28_29_day_month = [2]

        leap_status = self.CheckLeap(self.count_year)
        first_day = zl.Zellercongruence(1, self.count + 1, self.count_year)

        label_id_list = ["row00_label", "row01_label", "row02_label", "row03_label", "row04_label", "row05_label", "row06_label",
                            "row10_label", "row11_label", "row12_label", "row13_label", "row14_label", "row15_label", "row16_label",
                            "row20_label", "row21_label", "row22_label", "row23_label", "row24_label", "row25_label", "row26_label",
                            "row30_label", "row31_label", "row32_label", "row33_label", "row34_label", "row35_label", "row36_label",
                            "row40_label", "row41_label", "row42_label", "row43_label", "row44_label", "row45_label", "row46_label",
                            "row50_label", "row51_label", "row52_label", "row53_label", "row54_label", "row55_label", "row56_label"]
        if month_number in _31_day_month:
            print("this month has 31 days")
            if first_day == "Monday":

                calendar_labels = []
                for i in range(1):
                    calendar_labels.append("")

                for i in range(1, 32): # 1-31
                    calendar_labels.append(str(i))
                
                for i in range(10):
                    calendar_labels.append("-")

                for index, label_id in enumerate(label_id_list):
                    item = self.ids[label_id]
                    item.text = calendar_labels[index]
            if first_day == "Tuesday":
                calendar_labels = []
                for i in range(2):
                    calendar_labels.append("")

                for i in range(1, 32): # 1-31
                    calendar_labels.append(str(i))
                
                for i in range(9):
                    calendar_labels.append("-")

                for index, label_id in enumerate(label_id_list):
                    item = self.ids[label_id]
                    item.text = calendar_labels[index]
            if first_day == "Wednesday":
                calendar_labels = []
                for i in range(3):
                    calendar_labels.append("")

                for i in range(1, 32): # 1-31
                    calendar_labels.append(str(i))
                
                for i in range(8):
                    calendar_labels.append("-")

                for index, label_id in enumerate(label_id_list):
                    item = self.ids[label_id]
                    item.text = calendar_labels[index]
            if first_day == "Thursday":
                calendar_labels = []
                for i in range(4):
                    calendar_labels.append("")

                for i in range(1, 32): # 1-31
                    calendar_labels.append(str(i))
                
                for i in range(7):
                    calendar_labels.append("-")

                for index, label_id in enumerate(label_id_list):
                    item = self.ids[label_id]
                    item.text = calendar_labels[index]
            if first_day == "Friday":
                calendar_labels = []
                for i in range(5):
                    calendar_labels.append("")

                for i in range(1, 32): # 1-31
                    calendar_labels.append(str(i))
                
                for i in range(6):
                    calendar_labels.append("-")

                for index, label_id in enumerate(label_id_list):
                    item = self.ids[label_id]
                    item.text = calendar_labels[index]
            if first_day == "Saturday":
                calendar_labels = []
                for i in range(6):
                    calendar_labels.append("")

                for i in range(1, 32): # 1-31
                    calendar_labels.append(str(i))
                
                for i in range(5):
                    calendar_labels.append("-")

                for index, label_id in enumerate(label_id_list):
                    item = self.ids[label_id]
                    item.text = calendar_labels[index]
            if first_day == "Sunday":
                calendar_labels = []
                for i in range(0):
                    calendar_labels.append("")

                for i in range(1, 32): # 1-31
                    calendar_labels.append(str(i))
                
                for i in range(11):
                    calendar_labels.append("-")

                for index, label_id in enumerate(label_id_list):
                    item = self.ids[label_id]
                    item.text = calendar_labels[index]
        elif month_number in _30_day_month:
            print("this month has 30 days")
            if first_day == "Monday":
                calendar_labels = []
                for i in range(1):
                    calendar_labels.append("")

                for i in range(1, 31): # 1-31
                    calendar_labels.append(str(i))
                
                for i in range(11):
                    calendar_labels.append("-")

                for index, label_id in enumerate(label_id_list):
                    item = self.ids[label_id]
                    item.text = calendar_labels[index]
            if first_day == "Tuesday":
                calendar_labels = []
                for i in range(2):
                    calendar_labels.append("")

                for i in range(1, 31): # 1-31
                    calendar_labels.append(str(i))
                
                for i in range(10):
                    calendar_labels.append("-")

                for index, label_id in enumerate(label_id_list):
                    item = self.ids[label_id]
                    item.text = calendar_labels[index]
            if first_day == "Wednesday":
                calendar_labels = []
                for i in range(3):
                    calendar_labels.append("")

                for i in range(1, 31): # 1-31
                    calendar_labels.append(str(i))
                
                for i in range(9):
                    calendar_labels.append("-")

                for index, label_id in enumerate(label_id_list):
                    item = self.ids[label_id]
                    item.text = calendar_labels[index]
            if first_day == "Thursday":
                calendar_labels = []
                for i in range(4):
                    calendar_labels.append("")

                for i in range(1, 31): # 1-31
                    calendar_labels.append(str(i))
                
                for i in range(8):
                    calendar_labels.append("-")

                for index, label_id in enumerate(label_id_list):
                    item = self.ids[label_id]
                    item.text = calendar_labels[index]
            if first_day == "Friday":
                calendar_labels = []
                for i in range(5):
                    calendar_labels.append("")

                for i in range(1, 31): # 1-31
                    calendar_labels.append(str(i))
                
                for i in range(7):
                    calendar_labels.append("-")

                for index, label_id in enumerate(label_id_list):
                    item = self.ids[label_id]
                    item.text = calendar_labels[index]
            if first_day == "Saturday":
                calendar_labels = []
                for i in range(6):
                    calendar_labels.append("")

                for i in range(1, 31): # 1-31
                    calendar_labels.append(str(i))
                
                for i in range(6):
                    calendar_labels.append("-")

                for index, label_id in enumerate(label_id_list):
                    item = self.ids[label_id]
                    item.text = calendar_labels[index]
            if first_day == "Sunday":
                calendar_labels = []
                for i in range(0):
                    calendar_labels.append("")

                for i in range(1, 31): # 1-31
                    calendar_labels.append(str(i))
                
                for i in range(12):
                    calendar_labels.append("-")

                for index, label_id in enumerate(label_id_list):
                    item = self.ids[label_id]
                    item.text = calendar_labels[index]

        elif month_number in _28_29_day_month:
            if leap_status == True:
                print("this month has 29 days")
                if first_day == "Monday":
                    calendar_labels = []
                    for i in range(1):
                        calendar_labels.append("")

                    for i in range(1, 30): # 1-29
                        calendar_labels.append(str(i))
                    
                    for i in range(12):
                        calendar_labels.append("-")

                    for index, label_id in enumerate(label_id_list):
                        item = self.ids[label_id]
                        item.text = calendar_labels[index]
                if first_day == "Tuesday":
                    calendar_labels = []
                    for i in range(2):
                        calendar_labels.append("")

                    for i in range(1, 30): # 1-29
                        calendar_labels.append(str(i))
                    
                    for i in range(11):
                        calendar_labels.append("-")

                    for index, label_id in enumerate(label_id_list):
                        item = self.ids[label_id]
                        item.text = calendar_labels[index]
                if first_day == "Wednesday":
                    calendar_labels = []
                    for i in range(3):
                        calendar_labels.append("")

                    for i in range(1, 30): # 1-29
                        calendar_labels.append(str(i))
                    
                    for i in range(10):
                        calendar_labels.append("-")

                    for index, label_id in enumerate(label_id_list):
                        item = self.ids[label_id]
                        item.text = calendar_labels[index]
                if first_day == "Thursday":
                    calendar_labels = []
                    for i in range(4):
                        calendar_labels.append("")

                    for i in range(1, 30): # 1-29
                        calendar_labels.append(str(i))
                    
                    for i in range(9):
                        calendar_labels.append("-")

                    for index, label_id in enumerate(label_id_list):
                        item = self.ids[label_id]
                        item.text = calendar_labels[index]
                if first_day == "Friday":
                    calendar_labels = []
                    for i in range(5):
                        calendar_labels.append("")

                    for i in range(1, 30): # 1-29
                        calendar_labels.append(str(i))
                    
                    for i in range(8):
                        calendar_labels.append("-")

                    for index, label_id in enumerate(label_id_list):
                        item = self.ids[label_id]
                        item.text = calendar_labels[index]
                if first_day == "Saturday":
                    calendar_labels = []
                    for i in range(6):
                        calendar_labels.append("")

                    for i in range(1, 30): # 1-29
                        calendar_labels.append(str(i))
                    
                    for i in range(7):
                        calendar_labels.append("-")

                    for index, label_id in enumerate(label_id_list):
                        item = self.ids[label_id]
                        item.text = calendar_labels[index]
                if first_day == "Sunday":
                    calendar_labels = []
                    for i in range(0):
                        calendar_labels.append("")

                    for i in range(1, 30): # 1-29
                        calendar_labels.append(str(i))
                    
                    for i in range(13):
                        calendar_labels.append("-")

                    for index, label_id in enumerate(label_id_list):
                        item = self.ids[label_id]
                        item.text = calendar_labels[index]
            else:
                print("this month has 28 days")
                if first_day == "Monday":
                    calendar_labels = []
                    for i in range(1):
                        calendar_labels.append("")

                    for i in range(1, 29): # 1-28
                        calendar_labels.append(str(i))
                    
                    for i in range(13):
                        calendar_labels.append("-")

                    for index, label_id in enumerate(label_id_list):
                        item = self.ids[label_id]
                        item.text = calendar_labels[index]
                if first_day == "Tuesday":
                    calendar_labels = []
                    for i in range(2):
                        calendar_labels.append("")

                    for i in range(1, 29): # 1-28
                        calendar_labels.append(str(i))
                    
                    for i in range(12):
                        calendar_labels.append("-")

                    for index, label_id in enumerate(label_id_list):
                        item = self.ids[label_id]
                        item.text = calendar_labels[index]
                if first_day == "Wednesday":
                    calendar_labels = []
                    for i in range(3):
                        calendar_labels.append("")

                    for i in range(1, 29): # 1-28
                        calendar_labels.append(str(i))
                    
                    for i in range(11):
                        calendar_labels.append("-")

                    for index, label_id in enumerate(label_id_list):
                        item = self.ids[label_id]
                        item.text = calendar_labels[index]

                if first_day == "Thursday":
                    calendar_labels = []
                    for i in range(4):
                        calendar_labels.append("")

                    for i in range(1, 29): # 1-28
                        calendar_labels.append(str(i))
                    
                    for i in range(10):
                        calendar_labels.append("-")

                    for index, label_id in enumerate(label_id_list):
                        item = self.ids[label_id]
                        item.text = calendar_labels[index]
                if first_day == "Friday":
                    calendar_labels = []
                    for i in range(5):
                        calendar_labels.append("")

                    for i in range(1, 29): # 1-28
                        calendar_labels.append(str(i))
                    
                    for i in range(9):
                        calendar_labels.append("-")

                    for index, label_id in enumerate(label_id_list):
                        item = self.ids[label_id]
                        item.text = calendar_labels[index]
                if first_day == "Saturday":
                    calendar_labels = []
                    for i in range(6):
                        calendar_labels.append("")

                    for i in range(1, 29): # 1-28
                        calendar_labels.append(str(i))
                    
                    for i in range(8):
                        calendar_labels.append("-")

                    for index, label_id in enumerate(label_id_list):
                        item = self.ids[label_id]
                        item.text = calendar_labels[index]
                if first_day == "Sunday":
                    calendar_labels = []
                    for i in range(0):
                        calendar_labels.append("")

                    for i in range(1, 29): # 1-28
                        calendar_labels.append(str(i))
                    
                    for i in range(14):
                        calendar_labels.append("-")

                    for index, label_id in enumerate(label_id_list):
                        item = self.ids[label_id]
                        item.text = calendar_labels[index]

    def CheckLeap(self, Year):
        # Checking if the given year is leap year
        if((Year % 400 == 0) or
            (Year % 100 != 0) and
            (Year % 4 == 0)):
            print("Given Year is a leap Year")
            return True
        # Else it is not a leap year
        else:
            print ("Given Year is not a leap Year")
            return False
    
    def color_date(self):
        this_day = date.today()
        datetime_split = str(this_day).split("-")

        day = int(datetime_split[2])
        month = int(datetime_split[1]) # 1 -> January
        year = int(datetime_split[0])

        mnth = self.count+1
        print("show me value ---> ", month, mnth, year, self.count_year)
        # check ว่า label อันไหนมี text เท่ากับตัวแปร date
        # ถ้าเจอ label id นั้นๆ ให้ใส่โค้ดสี
        label_id_list = ["row00_label", "row01_label", "row02_label", "row03_label", "row04_label", "row05_label", "row06_label",
                            "row10_label", "row11_label", "row12_label", "row13_label", "row14_label", "row15_label", "row16_label",
                            "row20_label", "row21_label", "row22_label", "row23_label", "row24_label", "row25_label", "row26_label",
                            "row30_label", "row31_label", "row32_label", "row33_label", "row34_label", "row35_label", "row36_label",
                            "row40_label", "row41_label", "row42_label", "row43_label", "row44_label", "row45_label", "row46_label",
                            "row50_label", "row51_label", "row52_label", "row53_label", "row54_label", "row55_label", "row56_label"]
        for label_id in label_id_list:
            date_label = self.ids[label_id]
            date_value = date_label.text
            if str(day) == date_value and str(month) == str(mnth) and str(year) == str(self.count_year):
                print("FOUND IT. >>>>>>>>")
                # ใส่สีให้กับ label
                date_label.color = "#fd2b81"
                date_label.bold = True
                date_label.font_size = '20sp'
                date_label.text = f"[i]{date_value}[/i]"
                date_label.markup = True
            else:
                date_label.color = 1, 1, 1, 1
                date_label.bold = False
                date_label.markup = False
                date_label.font_size = '15sp'
                
    def CallTextInput(self):
        print("Call text input is called.")
        year_input_str = self.ids.year_text_input.text
        if len(year_input_str) > 0 and len(year_input_str) <= 4:
            print("Valid input length.")
            # เช็คเรื่องตัวเลข / ตัวอักษรต่อ
            if year_input_str.isdigit():
                print("Valid input digit")
                self.count_year = int(year_input_str)
                print("count_year --> ", self.count_year)
                self.modify_calendar()

            else:
                print("Invalid input digit")
        else:
            print("Invalid input length.")

class WindowManager(ScreenManager):
    pass

class DesignVersion1App(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name="splash"))
        sm.add_widget(MainScreen(name="main"))
        return sm

if __name__ == "__main__":
    app = DesignVersion1App()
    app.run()