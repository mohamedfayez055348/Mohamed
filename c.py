from arabic_reshaper import*
from tkinter import*
from tkinter import messagebox
pro=Tk()
#خاصية التحكم في أبعاد النافذة
pro.geometry("680x1480")
#خاصية التحكم في العنوان
pro.title("Person Square")
#خاصية التحكم في خصائص النافذة (اللون)
pro.config(bg="#F7E1FF")
#متغيرات الوصول
#1-متغير الوصول الي نوع العملية والمربوط (opretor_type)
var_opretor_type=StringVar(value="Preparation")
#2-متغير الوصول الي نوع التركيز والمربوط (construction_type)
var_soulation_type=StringVar()
var_construction_type_main=StringVar()
var_construction_type_first=StringVar()
var_construction_type_second=StringVar()
#قائمة نوع العملية التي يرث منها راديو بوتون نوع العملية
opretor_type_list=("Mixing","Increase","Dilute","Preparation")
soulation_type_list=["Salad","Suggar"]
construction_type_list=("Salometer","Bomiat","Balng")#
def placeing():
	if var_opretor_type.get()=="Preparation":
		label_entry_main_construction.config(text=reshape("تركيز المحلول")[::-1])
		label_main_construction_type.config(text=reshape("أختر نوع التركيز")[::-1])
		calculate_button.place(x=250,y=690,height=60,width=200)
		label_entry_first_construction.place_forget()
		entry_first_construction.place_forget()
		label_first_construction_type.place_forget()
		construction_type_balng_first.place_forget()
		construction_type_bomiat_first.place_forget()
		construction_type_salometer_first.place_forget()
		label_entry_second_construction.place_forget()
		entry_second_construction.place_forget()
		label_second_construction_type.place_forget()
		construction_type_balng_second.place_forget()
		construction_type_bomiat_second.place_forget()
		construction_type_salometer_second.place_forget()
		entry_weight.delete(0,END)
		entry_main_construction.delete(0,END)
		entry_first_construction.delete(0,END)
		entry_second_construction.delete(0,END)
		label_result.config(text=f"")
	elif var_opretor_type.get()=="Dilute":
		label_first_construction_type.config(text=reshape("أختر نوع التركيز المنخفض")[::-1])
		label_entry_main_construction.config(text=reshape("التركيز المرتفع")[::-1])
		label_entry_first_construction.config(text=reshape("التركيز المنخفض")[::-1])
		label_main_construction_type.config(text=reshape("اختر نوع التركيز المرتفع")[::-1])
		label_entry_first_construction.place(x=1,y=190,width=325,height=50)
		entry_first_construction.place(x=330,y=190,width=345,height=50)
		label_first_construction_type.place(x=1,y=680,width=680)
		construction_type_balng_first.place(x=452,y=735,width=228)
		construction_type_bomiat_first.place(x=226,y=735,width=226)
		construction_type_salometer_first.place(x=1,y=735,width=226)
		calculate_button.place(x=250,y=800,height=60,width=200)
		label_entry_second_construction.place_forget()
		entry_second_construction.place_forget()
		label_second_construction_type.place_forget()
		construction_type_balng_second.place_forget()
		construction_type_bomiat_second.place_forget()
		construction_type_salometer_second.place_forget()
		entry_weight.delete(0,END)
		entry_main_construction.delete(0,END)
		entry_first_construction.delete(0,END)
		entry_second_construction.delete(0,END)
		label_result.config(text=f"")
	elif var_opretor_type.get()=="Increase":
		label_entry_main_construction.config(text=reshape("التركيز المنخفض")[::-1])
		label_entry_first_construction.config(text=reshape("التركيز المرتفع")[::-1])
		label_main_construction_type.config(text=reshape("أختر نوع التركيز المنخفض")[::-1])
		label_first_construction_type.config(text=reshape("اختر نوع التركيز المرتفع")[::-1])
		label_entry_first_construction.place(x=1,y=190,width=325,height=50)
		entry_first_construction.place(x=330,y=190,width=345,height=50)
		label_first_construction_type.place(x=1,y=680,width=680)
		construction_type_balng_first.place(x=452,y=735,width=228)
		construction_type_bomiat_first.place(x=226,y=735,width=226)
		construction_type_salometer_first.place(x=1,y=735,width=226)
		calculate_button.place(x=250,y=800,height=60,width=200)
		label_entry_second_construction.place_forget()
		entry_second_construction.place_forget()
		label_second_construction_type.place_forget()
		construction_type_balng_second.place_forget()
		construction_type_bomiat_second.place_forget()
		construction_type_salometer_second.place_forget()
		entry_weight.delete(0,END)
		entry_main_construction.delete(0,END)
		entry_first_construction.delete(0,END)
		entry_second_construction.delete(0,END)
		label_result.config(text=f"")
	else:
		label_main_construction_type.config(text=reshape("اختر نوع التركيز النهائي")[::-1])
		label_first_construction_type.config(text=reshape("اختر نوع التركيز الاول")[::-1])
		label_second_construction_type.config(text=reshape("اختر نوع التركيز الثاني")[::-1])
		label_entry_main_construction.config(text=reshape("التركيز النهائي")[::-1])
		label_entry_first_construction.config(text=reshape("التركيز الاول")[::-1])
		label_entry_second_construction.config(text=reshape("التركيز الثاني")[::-1])
		label_entry_first_construction.place(x=1,y=190,width=325,height=50)
		entry_first_construction.place(x=330,y=190,width=345,height=50)
		label_entry_second_construction.place(x=1,y=260,width=325,height=50)
		entry_second_construction.place(x=330,y=260,width=345,height=50)
		label_first_construction_type.place(x=1,y=680,width=680)
		label_second_construction_type.place(x=1,y=790,width=680)
		construction_type_balng_first.place(x=452,y=735,width=228)
		construction_type_bomiat_first.place(x=226,y=735,width=226)
		construction_type_salometer_first.place(x=1,y=735,width=226)
		construction_type_balng_second.place(x=452,y=845,width=228)
		construction_type_bomiat_second.place(x=226,y=845,width=226)
		construction_type_salometer_second.place(x=1,y=845,width=226)
		calculate_button.place(x=250,y=910,height=60,width=200)
		entry_weight.delete(0,END)
		entry_main_construction.delete(0,END)
		entry_first_construction.delete(0,END)
		entry_second_construction.delete(0,END)
		label_result.config(text=f"")

def culculate():
    if var_opretor_type.get()=="Preparation":
        if len(entry_weight.get())>0 and len(entry_main_construction.get())>0 and var_soulation_type.get() in soulation_type_list and var_construction_type_main.get() in construction_type_list:
            if var_soulation_type.get()== "Suggar" and var_construction_type_main.get() == "Balng":
                high_concentration = 100
                low_concentration = 0
                conversion = float(entry_main_construction.get())
                bombyx_conversion = conversion * 0.55
                water_concentration = high_concentration - conversion
                water_weight = (water_concentration * float(entry_weight.get())) / 100
                solid_concentration = (low_concentration - conversion) * -1
                solid_weight = (solid_concentration * float(entry_weight.get())) / 100
                solution_density = 145 / (145 - bombyx_conversion)
                solution_volume = float(entry_weight.get()) / solution_density
            elif var_soulation_type.get()== "Suggar" and var_construction_type_main.get() == "Bomiat":
                high_concentration = 100
                low_concentration = 0
                conversion = float(entry_main_construction.get())/0.55
                bombyx_conversion = conversion * 0.55
                water_concentration = high_concentration - conversion
                water_weight = (water_concentration * float(entry_weight.get())) / 100
                solid_concentration = (low_concentration - conversion) * -1
                solid_weight = (solid_concentration * float(entry_weight.get())) / 100
                solution_density = 145 / (145 - bombyx_conversion)
                solution_volume = float(entry_weight.get()) / solution_density
            elif var_soulation_type.get()== "Suggar" and var_construction_type_main.get() == "Salometer":
                high_concentration = 100
                low_concentration = 0
                conversion = float(entry_main_construction.get())/2.2
                bombyx_conversion = conversion * 0.55
                water_concentration = high_concentration - conversion
                water_weight = (water_concentration * float(entry_weight.get())) / 100
                solid_concentration = (low_concentration - conversion) * -1
                solid_weight = (solid_concentration * float(entry_weight.get())) / 100
                solution_density = 145 / (145 - bombyx_conversion)
                solution_volume = float(entry_weight.get()) / solution_density
            elif var_soulation_type.get()== "Salad" and var_construction_type_main.get() == "Bomiat":
                high_concentration = 100
                low_concentration = 0
                conversion = float(entry_main_construction.get())
                bombyx_conversion = conversion 
                water_concentration = high_concentration - conversion
                water_weight = (water_concentration * float(entry_weight.get())) / 100
                solid_concentration = (low_concentration - conversion) * -1
                solid_weight = (solid_concentration * float(entry_weight.get())) / 100
                solution_density = 145 / (145 - bombyx_conversion)
                solution_volume = float(entry_weight.get()) / solution_density
            elif var_soulation_type.get()== "Salad" and var_construction_type_main.get() == "Balng":
                high_concentration = 100
                low_concentration = 0
                conversion = float(entry_main_construction.get())*0.55
                bombyx_conversion = conversion 
                water_concentration = high_concentration - conversion
                water_weight = (water_concentration * float(entry_weight.get())) / 100
                solid_concentration = (low_concentration - conversion) * -1
                solid_weight = (solid_concentration * float(entry_weight.get())) / 100
                solution_density = 145 / (145 - bombyx_conversion)
                solution_volume = float(entry_weight.get()) / solution_density
            elif var_soulation_type.get()== "Salad" and var_construction_type_main.get() == "Salometer":
                high_concentration = 100
                low_concentration = 0
                conversion = float(entry_main_construction.get())/4
                bombyx_conversion = conversion 
                water_concentration = high_concentration - conversion
                water_weight = (water_concentration * float(entry_weight.get())) / 100
                solid_concentration = (low_concentration - conversion) * -1
                solid_weight = (solid_concentration * float(entry_weight.get())) / 100
                solution_density = 145 / (145 - bombyx_conversion)
                solution_volume = float(entry_weight.get()) / solution_density
            if var_soulation_type.get()== "Salad":
                soulation_type=reshape("ملحى")[::-1]
                soul = reshape("كمية الملح اللازمة لتحضير المحلول")[::-1]
                construction_type=reshape("بومية")[::-1]
            else :
                soulation_type=reshape("سكرى")[::-1]
                soul = reshape("كمية السكر اللازمة لتحضير المحلول")[::-1]
                construction_type=reshape("بالنج")[::-1]
            label_result.config(text=f"{reshape('كجم')[::-1]} {entry_weight.get()} = {reshape('وزن المحلول المطلوب تحضيره')[::-1]}\n{soulation_type} = {reshape('نوع المحلول المطلوب تحضيره')[::-1]}\n{construction_type} = {reshape('نوع تركيز المحلول المطلوب تحضيره')[::-1]}\n{construction_type} {conversion:.2f} = {reshape('تركيز المحلول المطلوب تحضيره')[::-1]}\n{reshape('كجم')[::-1]} {water_weight:.2f} = {reshape('كمية الماء اللازمة لتحضير المحلول')[::-1]}\n{reshape('كجم')[::-1]} {solid_weight:.2f} = {soul}\n{reshape('لتر')[::-1]} {solution_volume:.2f} = {reshape('حجم المحلول')[::-1]}\n{reshape('كجم/لتر')[::-1]} {solution_density:.2f} = {reshape('كثافة المحلول')[::-1]}")
        else:
	        messagebox.showinfo("Cutton",reshape("من فضلك أدخل جميع البيانات")[::-1])
    elif var_opretor_type.get()=="Dilute":
        if len(entry_weight.get())>0 and len(entry_main_construction.get())>0 and len(entry_first_construction.get())>0 and var_soulation_type.get() in soulation_type_list and  var_construction_type_main.get() in construction_type_list and  var_construction_type_first.get() in construction_type_list:
            if var_soulation_type.get() =="Suggar" and var_construction_type_main.get()=="Balng" and var_construction_type_first.get() =="Balng":
                high_concentration_solution=float(entry_main_construction.get()) # تركيز المحلول القديم المرتفع
                low_concentration_solution=float(entry_first_construction.get())
                water_concentration=0 # تركيز الماء
                old_conversion=high_concentration_solution # التركيز القديم المراد الرفع منه بعد التحويل الي التركيز المناسب
                new_conversion=low_concentration_solution # التركيز الجديد المراد الرفع اليه بعد التحويل الي التركيز المناسب
                start_water_weight=abs(old_conversion-new_conversion) # كمية الماء داخل بيرسون
                start_solution_weight=abs(water_concentration-new_conversion) #  كمية المادة الصلبة داخل بيرسون
                total_solution_weight=start_water_weight+start_solution_weight
                end_solution_weight=float(entry_weight.get())
                end_water_weight=(start_water_weight*end_solution_weight)/start_solution_weight
                end_solution_weight_finally=end_solution_weight+end_water_weight
                bombyx_conversion=new_conversion*0.55
                solution_density=145/(145-bombyx_conversion)
                solution_volume=end_solution_weight_finally/solution_density
                #label_result.config(text=f"Result\n{50*'*'}\nWeight of the solution before dilution = {end_solution_weight} Kg\nOld concentration to be reduced = {old_conversion:.2f} Balng\nNew concentration desired after dilution = {new_conversion:.2f} Balng\nAmount of water needed for dilution = {end_water_weight:.2f} Kg\nWeight of the solution after dilution = {end_solution_weight_finally:.2f} Kg\nVolume of the solution after dilution = {solution_volume:.2f} Liter\nDensity of the solution after dilution = {solution_density:.2f}Kg/Liter".title())
            elif var_soulation_type.get() =="Suggar" and var_construction_type_main.get()=="Balng" and var_construction_type_first.get() =="Bomiat":
                high_concentration_solution=float(entry_main_construction.get()) # تركيز المحلول القديم المرتفع
                low_concentration_solution=float(entry_first_construction.get())
                water_concentration=0 # تركيز الماء
                old_conversion=high_concentration_solution # التركيز القديم المراد الرفع منه بعد التحويل الي التركيز المناسب
                new_conversion=low_concentration_solution/0.55 # التركيز الجديد المراد الرفع اليه بعد التحويل الي التركيز المناسب
                start_water_weight=abs(old_conversion-new_conversion) # كمية الماء داخل بيرسون
                start_solution_weight=abs(water_concentration-new_conversion) #  كمية المادة الصلبة داخل بيرسون
                total_solution_weight=start_water_weight+start_solution_weight
                end_solution_weight=float(entry_weight.get())
                end_water_weight=(start_water_weight*end_solution_weight)/start_solution_weight
                end_solution_weight_finally=end_solution_weight+end_water_weight
                bombyx_conversion=new_conversion*0.55
                solution_density=145/(145-bombyx_conversion)
                solution_volume=end_solution_weight_finally/solution_density
            elif var_soulation_type.get() =="Suggar" and var_construction_type_main.get()=="Balng" and var_construction_type_first.get() =="Salometer":
                high_concentration_solution=float(entry_main_construction.get()) # تركيز المحلول القديم المرتفع
                low_concentration_solution=float(entry_first_construction.get())
                water_concentration=0 # تركيز الماء
                old_conversion=high_concentration_solution # التركيز القديم المراد الرفع منه بعد التحويل الي التركيز المناسب
                new_conversion=low_concentration_solution/2.2 # التركيز الجديد المراد الرفع اليه بعد التحويل الي التركيز المناسب
                start_water_weight=abs(old_conversion-new_conversion) # كمية الماء داخل بيرسون
                start_solution_weight=abs(water_concentration-new_conversion) #  كمية المادة الصلبة داخل بيرسون
                total_solution_weight=start_water_weight+start_solution_weight
                end_solution_weight=float(entry_weight.get())
                end_water_weight=(start_water_weight*end_solution_weight)/start_solution_weight
                end_solution_weight_finally=end_solution_weight+end_water_weight
                bombyx_conversion=new_conversion*0.55
                solution_density=145/(145-bombyx_conversion)
                solution_volume=end_solution_weight_finally/solution_density
            elif var_soulation_type.get() =="Suggar" and var_construction_type_main.get()=="Bomiat" and var_construction_type_first.get() =="Bomiat":
                high_concentration_solution=float(entry_main_construction.get()) # تركيز المحلول القديم المرتفع
                low_concentration_solution=float(entry_first_construction.get())
                water_concentration=0 # تركيز الماء
                old_conversion=high_concentration_solution/0.55 # التركيز القديم المراد الرفع منه بعد التحويل الي التركيز المناسب
                new_conversion=low_concentration_solution/0.55 # التركيز الجديد المراد الرفع اليه بعد التحويل الي التركيز المناسب
                start_water_weight=abs(old_conversion-new_conversion) # كمية الماء داخل بيرسون
                start_solution_weight=abs(water_concentration-new_conversion) #  كمية المادة الصلبة داخل بيرسون
                total_solution_weight=start_water_weight+start_solution_weight
                end_solution_weight=float(entry_weight.get())
                end_water_weight=(start_water_weight*end_solution_weight)/start_solution_weight
                end_solution_weight_finally=end_solution_weight+end_water_weight
                bombyx_conversion=new_conversion*0.55
                solution_density=145/(145-bombyx_conversion)
                solution_volume=end_solution_weight_finally/solution_density
            elif var_soulation_type.get() =="Suggar" and var_construction_type_main.get()=="Bomiat" and var_construction_type_first.get() =="Balng":
                high_concentration_solution=float(entry_main_construction.get()) # تركيز المحلول القديم المرتفع
                low_concentration_solution=float(entry_first_construction.get())
                water_concentration=0 # تركيز الماء
                old_conversion=high_concentration_solution/0.55 # التركيز القديم المراد الرفع منه بعد التحويل الي التركيز المناسب
                new_conversion=low_concentration_solution # التركيز الجديد المراد الرفع اليه بعد التحويل الي التركيز المناسب
                start_water_weight=abs(old_conversion-new_conversion) # كمية الماء داخل بيرسون
                start_solution_weight=abs(water_concentration-new_conversion) #  كمية المادة الصلبة داخل بيرسون
                total_solution_weight=start_water_weight+start_solution_weight
                end_solution_weight=float(entry_weight.get())
                end_water_weight=(start_water_weight*end_solution_weight)/start_solution_weight
                end_solution_weight_finally=end_solution_weight+end_water_weight
                bombyx_conversion=new_conversion*0.55
                solution_density=145/(145-bombyx_conversion)
                solution_volume=end_solution_weight_finally/solution_density
            elif var_soulation_type.get() =="Suggar" and var_construction_type_main.get()=="Bomiat" and var_construction_type_first.get() =="Salometer":
                high_concentration_solution=float(entry_main_construction.get()) # تركيز المحلول القديم المرتفع
                low_concentration_solution=float(entry_first_construction.get())
                water_concentration=0 # تركيز الماء
                old_conversion=high_concentration_solution/0.55 # التركيز القديم المراد الرفع منه بعد التحويل الي التركيز المناسب
                new_conversion=low_concentration_solution/2.2 # التركيز الجديد المراد الرفع اليه بعد التحويل الي التركيز المناسب
                start_water_weight=abs(old_conversion-new_conversion) # كمية الماء داخل بيرسون
                start_solution_weight=abs(water_concentration-new_conversion) #  كمية المادة الصلبة داخل بيرسون
                total_solution_weight=start_water_weight+start_solution_weight
                end_solution_weight=float(entry_weight.get())
                end_water_weight=(start_water_weight*end_solution_weight)/start_solution_weight
                end_solution_weight_finally=end_solution_weight+end_water_weight
                bombyx_conversion=new_conversion*0.55
                solution_density=145/(145-bombyx_conversion)
                solution_volume=end_solution_weight_finally/solution_density
            elif var_soulation_type.get() =="Suggar" and var_construction_type_main.get()=="Salometer" and var_construction_type_first.get() =="Salometer":
                type="Balng"
                high_concentration_solution=float(entry_main_construction.get()) # تركيز المحلول القديم المرتفع
                low_concentration_solution=float(entry_first_construction.get())
                water_concentration=0 # تركيز الماء
                old_conversion=high_concentration_solution/2.2 # التركيز القديم المراد الرفع منه بعد التحويل الي التركيز المناسب
                new_conversion=low_concentration_solution/2.2 # التركيز الجديد المراد الرفع اليه بعد التحويل الي التركيز المناسب
                start_water_weight=abs(old_conversion-new_conversion) # كمية الماء داخل بيرسون
                start_solution_weight=abs(water_concentration-new_conversion) #  كمية المادة الصلبة داخل بيرسون
                total_solution_weight=start_water_weight+start_solution_weight
                end_solution_weight=float(entry_weight.get())
                end_water_weight=(start_water_weight*end_solution_weight)/start_solution_weight
                end_solution_weight_finally=end_solution_weight+end_water_weight
                bombyx_conversion=new_conversion*0.55
                solution_density=145/(145-bombyx_conversion)
                solution_volume=end_solution_weight_finally/solution_density
            elif var_soulation_type.get() =="Suggar" and var_construction_type_main.get()=="Salometer" and var_construction_type_first.get() =="Balng":
                type="Balng"
                high_concentration_solution=float(entry_main_construction.get()) # تركيز المحلول القديم المرتفع
                low_concentration_solution=float(entry_first_construction.get())
                water_concentration=0 # تركيز الماء
                old_conversion=high_concentration_solution/2.2 # التركيز القديم المراد الرفع منه بعد التحويل الي التركيز المناسب
                new_conversion=low_concentration_solution # التركيز الجديد المراد الرفع اليه بعد التحويل الي التركيز المناسب
                start_water_weight=abs(old_conversion-new_conversion) # كمية الماء داخل بيرسون
                start_solution_weight=abs(water_concentration-new_conversion) #  كمية المادة الصلبة داخل بيرسون
                total_solution_weight=start_water_weight+start_solution_weight
                end_solution_weight=float(entry_weight.get())
                end_water_weight=(start_water_weight*end_solution_weight)/start_solution_weight
                end_solution_weight_finally=end_solution_weight+end_water_weight
                bombyx_conversion=new_conversion*0.55
                solution_density=145/(145-bombyx_conversion)
                solution_volume=end_solution_weight_finally/solution_density
            elif var_soulation_type.get() =="Suggar" and var_construction_type_main.get()=="Salometer" and var_construction_type_first.get() =="Bomiat":
                type="Balng"
                high_concentration_solution=float(entry_main_construction.get()) # تركيز المحلول القديم المرتفع
                low_concentration_solution=float(entry_first_construction.get())
                water_concentration=0 # تركيز الماء
                old_conversion=high_concentration_solution/2.2 # التركيز القديم المراد الرفع منه بعد التحويل الي التركيز المناسب
                new_conversion=low_concentration_solution/0.55 # التركيز الجديد المراد الرفع اليه بعد التحويل الي التركيز المناسب
                start_water_weight=abs(old_conversion-new_conversion) # كمية الماء داخل بيرسون
                start_solution_weight=abs(water_concentration-new_conversion) #  كمية المادة الصلبة داخل بيرسون
                total_solution_weight=start_water_weight+start_solution_weight
                end_solution_weight=float(entry_weight.get())
                end_water_weight=(start_water_weight*end_solution_weight)/start_solution_weight
                end_solution_weight_finally=end_solution_weight+end_water_weight
                bombyx_conversion=new_conversion*0.55
                solution_density=145/(145-bombyx_conversion)
                solution_volume=end_solution_weight_finally/solution_density
            elif var_soulation_type.get() =="Salad" and var_construction_type_main.get()=="Balng" and var_construction_type_first.get() =="Balng":
                type="Bomiat"
                high_concentration_solution=float(entry_main_construction.get()) # تركيز المحلول القديم المرتفع
                low_concentration_solution=float(entry_first_construction.get())
                water_concentration=0 # تركيز الماء
                old_conversion=high_concentration_solution*0.55 # التركيز القديم المراد الرفع منه بعد التحويل الي التركيز المناسب
                new_conversion=low_concentration_solution*0.55 # التركيز الجديد المراد الرفع اليه بعد التحويل الي التركيز المناسب
                start_water_weight=abs(old_conversion-new_conversion) # كمية الماء داخل بيرسون
                start_solution_weight=abs(water_concentration-new_conversion) #  كمية المادة الصلبة داخل بيرسون
                total_solution_weight=start_water_weight+start_solution_weight
                end_solution_weight=float(entry_weight.get())
                end_water_weight=(start_water_weight*end_solution_weight)/start_solution_weight
                end_solution_weight_finally=end_solution_weight+end_water_weight
                bombyx_conversion=new_conversion
                solution_density=145/(145-bombyx_conversion)
                solution_volume=end_solution_weight_finally/solution_density
            elif var_soulation_type.get() =="Salad" and var_construction_type_main.get()=="Balng" and var_construction_type_first.get() =="Bomiat":
                type="Bomiat"
                high_concentration_solution=float(entry_main_construction.get()) # تركيز المحلول القديم المرتفع
                low_concentration_solution=float(entry_first_construction.get())
                water_concentration=0 # تركيز الماء
                old_conversion=high_concentration_solution*0.55 # التركيز القديم المراد الرفع منه بعد التحويل الي التركيز المناسب
                new_conversion=low_concentration_solution # التركيز الجديد المراد الرفع اليه بعد التحويل الي التركيز المناسب
                start_water_weight=abs(old_conversion-new_conversion) # كمية الماء داخل بيرسون
                start_solution_weight=abs(water_concentration-new_conversion) #  كمية المادة الصلبة داخل بيرسون
                total_solution_weight=start_water_weight+start_solution_weight
                end_solution_weight=float(entry_weight.get())
                end_water_weight=(start_water_weight*end_solution_weight)/start_solution_weight
                end_solution_weight_finally=end_solution_weight+end_water_weight
                bombyx_conversion=new_conversion
                solution_density=145/(145-bombyx_conversion)
                solution_volume=end_solution_weight_finally/solution_density
            elif var_soulation_type.get() =="Salad" and var_construction_type_main.get()=="Balng" and var_construction_type_first.get() =="Salometer":
                type="Bomiat"
                high_concentration_solution=float(entry_main_construction.get()) # تركيز المحلول القديم المرتفع
                low_concentration_solution=float(entry_first_construction.get())
                water_concentration=0 # تركيز الماء
                old_conversion=high_concentration_solution*0.55 # التركيز القديم المراد الرفع منه بعد التحويل الي التركيز المناسب
                new_conversion=low_concentration_solution/4 # التركيز الجديد المراد الرفع اليه بعد التحويل الي التركيز المناسب
                start_water_weight=abs(old_conversion-new_conversion) # كمية الماء داخل بيرسون
                start_solution_weight=abs(water_concentration-new_conversion) #  كمية المادة الصلبة داخل بيرسون
                total_solution_weight=start_water_weight+start_solution_weight
                end_solution_weight=float(entry_weight.get())
                end_water_weight=(start_water_weight*end_solution_weight)/start_solution_weight
                end_solution_weight_finally=end_solution_weight+end_water_weight
                bombyx_conversion=new_conversion
                solution_density=145/(145-bombyx_conversion)
                solution_volume=end_solution_weight_finally/solution_density
            elif var_soulation_type.get() =="Salad" and var_construction_type_main.get()=="Bomiat" and var_construction_type_first.get() =="Bomiat":
                type="Bomiat"
                high_concentration_solution=float(entry_main_construction.get()) # تركيز المحلول القديم المرتفع
                low_concentration_solution=float(entry_first_construction.get())
                water_concentration=0 # تركيز الماء
                old_conversion=high_concentration_solution # التركيز القديم المراد الرفع منه بعد التحويل الي التركيز المناسب
                new_conversion=low_concentration_solution # التركيز الجديد المراد الرفع اليه بعد التحويل الي التركيز المناسب
                start_water_weight=abs(old_conversion-new_conversion) # كمية الماء داخل بيرسون
                start_solution_weight=abs(water_concentration-new_conversion) #  كمية المادة الصلبة داخل بيرسون
                total_solution_weight=start_water_weight+start_solution_weight
                end_solution_weight=float(entry_weight.get())
                end_water_weight=(start_water_weight*end_solution_weight)/start_solution_weight
                end_solution_weight_finally=end_solution_weight+end_water_weight
                bombyx_conversion=new_conversion
                solution_density=145/(145-bombyx_conversion)
                solution_volume=end_solution_weight_finally/solution_density
            elif var_soulation_type.get() =="Salad" and var_construction_type_main.get()=="Bomiat" and var_construction_type_first.get() =="Balng":
                type="Bomiat"
                high_concentration_solution=float(entry_main_construction.get()) # تركيز المحلول القديم المرتفع
                low_concentration_solution=float(entry_first_construction.get())
                water_concentration=0 # تركيز الماء
                old_conversion=high_concentration_solution # التركيز القديم المراد الرفع منه بعد التحويل الي التركيز المناسب
                new_conversion=low_concentration_solution*0.55 # التركيز الجديد المراد الرفع اليه بعد التحويل الي التركيز المناسب
                start_water_weight=abs(old_conversion-new_conversion) # كمية الماء داخل بيرسون
                start_solution_weight=abs(water_concentration-new_conversion) #  كمية المادة الصلبة داخل بيرسون
                total_solution_weight=start_water_weight+start_solution_weight
                end_solution_weight=float(entry_weight.get())
                end_water_weight=(start_water_weight*end_solution_weight)/start_solution_weight
                end_solution_weight_finally=end_solution_weight+end_water_weight
                bombyx_conversion=new_conversion
                solution_density=145/(145-bombyx_conversion)
                solution_volume=end_solution_weight_finally/solution_density
            elif var_soulation_type.get() =="Salad" and var_construction_type_main.get()=="Bomiat" and var_construction_type_first.get() =="Salometer":
                type="Bomiat"
                high_concentration_solution=float(entry_main_construction.get()) # تركيز المحلول القديم المرتفع
                low_concentration_solution=float(entry_first_construction.get())
                water_concentration=0 # تركيز الماء
                old_conversion=high_concentration_solution # التركيز القديم المراد الرفع منه بعد التحويل الي التركيز المناسب
                new_conversion=low_concentration_solution/4 # التركيز الجديد المراد الرفع اليه بعد التحويل الي التركيز المناسب
                start_water_weight=abs(old_conversion-new_conversion) # كمية الماء داخل بيرسون
                start_solution_weight=abs(water_concentration-new_conversion) #  كمية المادة الصلبة داخل بيرسون
                total_solution_weight=start_water_weight+start_solution_weight
                end_solution_weight=float(entry_weight.get())
                end_water_weight=(start_water_weight*end_solution_weight)/start_solution_weight
                end_solution_weight_finally=end_solution_weight+end_water_weight
                bombyx_conversion=new_conversion
                solution_density=145/(145-bombyx_conversion)
                solution_volume=end_solution_weight_finally/solution_density
            elif var_soulation_type.get() =="Salad" and var_construction_type_main.get()=="Salometer" and var_construction_type_first.get() =="Salometer":
                type="Bomiat"
                high_concentration_solution=float(entry_main_construction.get()) # تركيز المحلول القديم المرتفع
                low_concentration_solution=float(entry_first_construction.get())
                water_concentration=0 # تركيز الماء
                old_conversion=high_concentration_solution/4 # التركيز القديم المراد الرفع منه بعد التحويل الي التركيز المناسب
                new_conversion=low_concentration_solution/4 # التركيز الجديد المراد الرفع اليه بعد التحويل الي التركيز المناسب
                start_water_weight=abs(old_conversion-new_conversion) # كمية الماء داخل بيرسون
                start_solution_weight=abs(water_concentration-new_conversion) #  كمية المادة الصلبة داخل بيرسون
                total_solution_weight=start_water_weight+start_solution_weight
                end_solution_weight=float(entry_weight.get())
                end_water_weight=(start_water_weight*end_solution_weight)/start_solution_weight
                end_solution_weight_finally=end_solution_weight+end_water_weight
                bombyx_conversion=new_conversion
                solution_density=145/(145-bombyx_conversion)
                solution_volume=end_solution_weight_finally/solution_density
            elif var_soulation_type.get() =="Salad" and var_construction_type_main.get()=="Salometer" and var_construction_type_first.get() =="Bomiat":
                type="Bomiat"
                high_concentration_solution=float(entry_main_construction.get()) # تركيز المحلول القديم المرتفع
                low_concentration_solution=float(entry_first_construction.get())
                water_concentration=0 # تركيز الماء
                old_conversion=high_concentration_solution/4 # التركيز القديم المراد الرفع منه بعد التحويل الي التركيز المناسب
                new_conversion=low_concentration_solution # التركيز الجديد المراد الرفع اليه بعد التحويل الي التركيز المناسب
                start_water_weight=abs(old_conversion-new_conversion) # كمية الماء داخل بيرسون
                start_solution_weight=abs(water_concentration-new_conversion) #  كمية المادة الصلبة داخل بيرسون
                total_solution_weight=start_water_weight+start_solution_weight
                end_solution_weight=float(entry_weight.get())
                end_water_weight=(start_water_weight*end_solution_weight)/start_solution_weight
                end_solution_weight_finally=end_solution_weight+end_water_weight
                bombyx_conversion=new_conversion
                solution_density=145/(145-bombyx_conversion)
                solution_volume=end_solution_weight_finally/solution_density
            elif var_soulation_type.get() =="Salad" and var_construction_type_main.get()=="Salometer" and var_construction_type_first.get() =="Balng":
                type="Bomiat"
                high_concentration_solution=float(entry_main_construction.get()) # تركيز المحلول القديم المرتفع
                low_concentration_solution=float(entry_first_construction.get())
                water_concentration=0 # تركيز الماء
                old_conversion=high_concentration_solution/4 # التركيز القديم المراد الرفع منه بعد التحويل الي التركيز المناسب
                new_conversion=low_concentration_solution*0.55 # التركيز الجديد المراد الرفع اليه بعد التحويل الي التركيز المناسب
                start_water_weight=abs(old_conversion-new_conversion) # كمية الماء داخل بيرسون
                start_solution_weight=abs(water_concentration-new_conversion) #  كمية المادة الصلبة داخل بيرسون
                total_solution_weight=start_water_weight+start_solution_weight
                end_solution_weight=float(entry_weight.get())
                end_water_weight=(start_water_weight*end_solution_weight)/start_solution_weight
                end_solution_weight_finally=end_solution_weight+end_water_weight
                bombyx_conversion=new_conversion
                solution_density=145/(145-bombyx_conversion)
                solution_volume=end_solution_weight_finally/solution_density
            if var_soulation_type.get()== "Salad":
                soulation_type=reshape("ملحى")[::-1]
                soul = reshape("كمية الملح اللازمة لتحضير المحلول")[::-1]
                construction_type=reshape("بومية")[::-1]
            else :
                soulation_type=reshape("سكرى")[::-1]
                soul = reshape("كمية السكر اللازمة لتحضير المحلول")[::-1]
                construction_type=reshape("بالنج")[::-1]

            label_result.config(text=f"{soulation_type} = {reshape('نوع المحلول المطلوب خفض تركيزه')[::-1]}\n{reshape('كجم')[::-1]} {end_solution_weight} = {reshape('وزن المحلول قبل خفض تركيزه')[::-1]}\n{construction_type} {old_conversion:.2f} = {reshape('التركيز القديم قبل الخفض')[::-1]}\n{construction_type} {new_conversion:.2f} = {reshape('التركيز الجديد بعد الخفض')[::-1]}\n{reshape('كجم')[::-1]} {end_water_weight:.2f} = {reshape('كمية الماء اللازم اضافتها لخفض تركيز المحلول')[::-1]}\n{reshape('كجم')[::-1]} {end_solution_weight_finally:.2f} = {reshape('الوزن النهائي للمحلول بعد خفض تركيزه')[::-1]}\n{reshape('لتر')[::-1]} {solution_volume:.2f} = {reshape('حجم المحلول بعد خفض تركيزه')[::-1]}\n{reshape('كجم/لتر')[::-1]} {solution_density:.2f} = {reshape('كثافة المحلول بعد خفض تركيزه')[::-1]}")
                    
            #label_result.config(text=f"{reshape('كجم')[::-1]} {entry_weight.get()} = {reshape('وزن المحلول المطلوب تحضيره')[::-1]}\n{soulation_type} = {reshape('نوع المحلول المطلوب تحضيره')[::-1]}\n{construction_type} = {reshape('نوع تركيز المحلول المطلوب تحضيره')[::-1]}\n{construction_type} {conversion:.2f} = {reshape('تركيز المحلول المطلوب تحضيره')[::-1]}\n{reshape('كجم')[::-1]} {water_weight:.2f} = {reshape('كمية الماء اللازمة لتحضير المحلول')[::-1]}\n{reshape('كجم')[::-1]} {solid_weight:.2f} = {soul}\n{reshape('لتر')[::-1]} {solution_volume:.2f} = {reshape('حجم المحلول')[::-1]}\n{reshape('كجم/لتر')[::-1]} {solution_density:.2f} = {reshape('كثافة المحلول')[::-1]}")

        else:
            messagebox.showinfo("Cutton",reshape("من فضلك أدخل جميع البيانات")[::-1])
    elif var_opretor_type.get()=="Increase":
         if len(entry_weight.get())>0 and len(entry_main_construction.get())>0 and len(entry_first_construction.get())>0 and var_soulation_type.get() in soulation_type_list and  var_construction_type_main.get() in construction_type_list and  var_construction_type_first.get() in construction_type_list:
         	if var_soulation_type.get() =="Suggar" and var_construction_type_main.get()=="Balng" and var_construction_type_first.get() =="Balng":
         		type="Balng"
         		high_concentration_soild=100
         		low_concentration=float(entry_main_construction.get())
         		high_concentration=float(entry_first_construction.get())
         		old_conversion=low_concentration
         		new_conversion=high_concentration
         		start_solution_weight=high_concentration_soild-new_conversion
         		start_soild_weight=abs(old_conversion-new_conversion)
         		end_solution_weight=float(entry_weight.get())
         		end_soild_weight=(start_soild_weight*end_solution_weight)/start_solution_weight
         		bombyx_conversion=new_conversion*0.55
         		solution_density=145/(145-bombyx_conversion)
         		finally_solution_weight=end_solution_weight+end_soild_weight
         		solution_volume=finally_solution_weight/solution_density
         	elif var_soulation_type.get() =="Suggar" and var_construction_type_main.get()=="Balng" and var_construction_type_first.get() =="Bomiat":
         		type="Balng"
         		high_concentration_soild=100
         		low_concentration=float(entry_main_construction.get())
         		high_concentration=float(entry_first_construction.get())/0.55
         		old_conversion=low_concentration
         		new_conversion=high_concentration
         		start_solution_weight=high_concentration_soild-new_conversion
         		start_soild_weight=abs(old_conversion-new_conversion)
         		end_solution_weight=float(entry_weight.get())
         		end_soild_weight=(start_soild_weight*end_solution_weight)/start_solution_weight
         		bombyx_conversion=new_conversion*0.55
         		solution_density=145/(145-bombyx_conversion)
         		finally_solution_weight=end_solution_weight+end_soild_weight
         		solution_volume=finally_solution_weight/solution_density
         	elif var_soulation_type.get() =="Suggar" and var_construction_type_main.get()=="Balng" and var_construction_type_first.get() =="Salometer":
         		type="Balng"
         		high_concentration_soild=100
         		low_concentration=float(entry_main_construction.get())
         		high_concentration=float(entry_first_construction.get())/2.2
         		old_conversion=low_concentration
         		new_conversion=high_concentration
         		start_solution_weight=high_concentration_soild-new_conversion
         		start_soild_weight=abs(old_conversion-new_conversion)
         		end_solution_weight=float(entry_weight.get())
         		end_soild_weight=(start_soild_weight*end_solution_weight)/start_solution_weight
         		bombyx_conversion=new_conversion*0.55
         		solution_density=145/(145-bombyx_conversion)
         		finally_solution_weight=end_solution_weight+end_soild_weight
         		solution_volume=finally_solution_weight/solution_density
         	elif var_soulation_type.get() =="Suggar" and var_construction_type_main.get()=="Bomiat" and var_construction_type_first.get() =="Bomiat":
         		type="Balng"
         		high_concentration_soild=100
         		low_concentration=float(entry_main_construction.get())/0.55
         		high_concentration=float(entry_first_construction.get())/0.55
         		old_conversion=low_concentration
         		new_conversion=high_concentration
         		start_solution_weight=high_concentration_soild-new_conversion
         		start_soild_weight=abs(old_conversion-new_conversion)
         		end_solution_weight=float(entry_weight.get())
         		end_soild_weight=(start_soild_weight*end_solution_weight)/start_solution_weight
         		bombyx_conversion=new_conversion*0.55
         		solution_density=145/(145-bombyx_conversion)
         		finally_solution_weight=end_solution_weight+end_soild_weight
         		solution_volume=finally_solution_weight/solution_density
         	elif var_soulation_type.get() =="Suggar" and var_construction_type_main.get()=="Bomiat" and var_construction_type_first.get() =="Balng":
         		type="Balng"
         		high_concentration_soild=100
         		low_concentration=float(entry_main_construction.get())/0.55
         		high_concentration=float(entry_first_construction.get())
         		old_conversion=low_concentration
         		new_conversion=high_concentration
         		start_solution_weight=high_concentration_soild-new_conversion
         		start_soild_weight=abs(old_conversion-new_conversion)
         		end_solution_weight=float(entry_weight.get())
         		end_soild_weight=(start_soild_weight*end_solution_weight)/start_solution_weight
         		bombyx_conversion=new_conversion*0.55
         		solution_density=145/(145-bombyx_conversion)
         		finally_solution_weight=end_solution_weight+end_soild_weight
         		solution_volume=finally_solution_weight/solution_density
         	elif var_soulation_type.get() =="Suggar" and var_construction_type_main.get()=="Bomiat" and var_construction_type_first.get() =="Salometer":
         		type="Balng"
         		high_concentration_soild=100
         		low_concentration=float(entry_main_construction.get())/0.55
         		high_concentration=float(entry_first_construction.get())/2.2
         		old_conversion=low_concentration
         		new_conversion=high_concentration
         		start_solution_weight=high_concentration_soild-new_conversion
         		start_soild_weight=abs(old_conversion-new_conversion)
         		end_solution_weight=float(entry_weight.get())
         		end_soild_weight=(start_soild_weight*end_solution_weight)/start_solution_weight
         		bombyx_conversion=new_conversion*0.55
         		solution_density=145/(145-bombyx_conversion)
         		finally_solution_weight=end_solution_weight+end_soild_weight
         		solution_volume=finally_solution_weight/solution_density
         	elif var_soulation_type.get() =="Suggar" and var_construction_type_main.get()=="Salometer" and var_construction_type_first.get() =="Salometer":
         		type="Balng"
         		high_concentration_soild=100
         		low_concentration=float(entry_main_construction.get())/2.2
         		high_concentration=float(entry_first_construction.get())/2.2
         		old_conversion=low_concentration
         		new_conversion=high_concentration
         		start_solution_weight=high_concentration_soild-new_conversion
         		start_soild_weight=abs(old_conversion-new_conversion)
         		end_solution_weight=float(entry_weight.get())
         		end_soild_weight=(start_soild_weight*end_solution_weight)/start_solution_weight
         		bombyx_conversion=new_conversion*0.55
         		solution_density=145/(145-bombyx_conversion)
         		finally_solution_weight=end_solution_weight+end_soild_weight
         		solution_volume=finally_solution_weight/solution_density
         	elif var_soulation_type.get() =="Suggar" and var_construction_type_main.get()=="Salometer" and var_construction_type_first.get() =="Bomiat":
         		type="Balng"
         		high_concentration_soild=100
         		low_concentration=float(entry_main_construction.get())/2.2
         		high_concentration=float(entry_first_construction.get())/0.55
         		old_conversion=low_concentration
         		new_conversion=high_concentration
         		start_solution_weight=high_concentration_soild-new_conversion
         		start_soild_weight=abs(old_conversion-new_conversion)
         		end_solution_weight=float(entry_weight.get())
         		end_soild_weight=(start_soild_weight*end_solution_weight)/start_solution_weight
         		bombyx_conversion=new_conversion*0.55
         		solution_density=145/(145-bombyx_conversion)
         		finally_solution_weight=end_solution_weight+end_soild_weight
         		solution_volume=finally_solution_weight/solution_density
         	elif var_soulation_type.get() =="Suggar" and var_construction_type_main.get()=="Salometer" and var_construction_type_first.get() =="Balng":
         		type="Balng"
         		high_concentration_soild=100
         		low_concentration=float(entry_main_construction.get())/2.2
         		high_concentration=float(entry_first_construction.get())
         		old_conversion=low_concentration
         		new_conversion=high_concentration
         		start_solution_weight=high_concentration_soild-new_conversion
         		start_soild_weight=abs(old_conversion-new_conversion)
         		end_solution_weight=float(entry_weight.get())
         		end_soild_weight=(start_soild_weight*end_solution_weight)/start_solution_weight
         		bombyx_conversion=new_conversion*0.55
         		solution_density=145/(145-bombyx_conversion)
         		finally_solution_weight=end_solution_weight+end_soild_weight
         		solution_volume=finally_solution_weight/solution_density
         	elif var_soulation_type.get() =="Salad" and var_construction_type_main.get()=="Bomiat" and var_construction_type_first.get() =="Bomiat":
         		type="Bomiat"
         		high_concentration_soild=100
         		low_concentration=float(entry_main_construction.get())
         		high_concentration=float(entry_first_construction.get())
         		old_conversion=low_concentration
         		new_conversion=high_concentration
         		start_solution_weight=high_concentration_soild-new_conversion
         		start_soild_weight=abs(old_conversion-new_conversion)
         		end_solution_weight=float(entry_weight.get())
         		end_soild_weight=(start_soild_weight*end_solution_weight)/start_solution_weight
         		bombyx_conversion=new_conversion
         		solution_density=145/(145-bombyx_conversion)
         		finally_solution_weight=end_solution_weight+end_soild_weight
         		solution_volume=finally_solution_weight/solution_density
         	elif var_soulation_type.get() =="Salad" and var_construction_type_main.get()=="Bomiat" and var_construction_type_first.get() =="Balng":
         		type="Bomiat"
         		high_concentration_soild=100
         		low_concentration=float(entry_main_construction.get())
         		high_concentration=float(entry_first_construction.get())*0.55
         		old_conversion=low_concentration
         		new_conversion=high_concentration
         		start_solution_weight=high_concentration_soild-new_conversion
         		start_soild_weight=abs(old_conversion-new_conversion)
         		end_solution_weight=float(entry_weight.get())
         		end_soild_weight=(start_soild_weight*end_solution_weight)/start_solution_weight
         		bombyx_conversion=new_conversion
         		solution_density=145/(145-bombyx_conversion)
         		finally_solution_weight=end_solution_weight+end_soild_weight
         		solution_volume=finally_solution_weight/solution_density
         	elif var_soulation_type.get() =="Salad" and var_construction_type_main.get()=="Bomiat" and var_construction_type_first.get() =="Salometer":
         		type="Bomiat"
         		high_concentration_soild=100
         		low_concentration=float(entry_main_construction.get())
         		high_concentration=float(entry_first_construction.get())/4
         		old_conversion=low_concentration
         		new_conversion=high_concentration
         		start_solution_weight=high_concentration_soild-new_conversion
         		start_soild_weight=abs(old_conversion-new_conversion)
         		end_solution_weight=float(entry_weight.get())
         		end_soild_weight=(start_soild_weight*end_solution_weight)/start_solution_weight
         		bombyx_conversion=new_conversion
         		solution_density=145/(145-bombyx_conversion)
         		finally_solution_weight=end_solution_weight+end_soild_weight
         		solution_volume=finally_solution_weight/solution_density
         	elif var_soulation_type.get() =="Salad" and var_construction_type_main.get()=="Balng" and var_construction_type_first.get() =="Balng":
         		type="Bomiat"
         		high_concentration_soild=100
         		low_concentration=float(entry_main_construction.get())*0.55
         		high_concentration=float(entry_first_construction.get())*0.55
         		old_conversion=low_concentration
         		new_conversion=high_concentration
         		start_solution_weight=high_concentration_soild-new_conversion
         		start_soild_weight=abs(old_conversion-new_conversion)
         		end_solution_weight=float(entry_weight.get())
         		end_soild_weight=(start_soild_weight*end_solution_weight)/start_solution_weight
         		bombyx_conversion=new_conversion
         		solution_density=145/(145-bombyx_conversion)
         		finally_solution_weight=end_solution_weight+end_soild_weight
         		solution_volume=finally_solution_weight/solution_density
         	elif var_soulation_type.get() =="Salad" and var_construction_type_main.get()=="Balng" and var_construction_type_first.get() =="Bomiat":
         		type="Bomiat"
         		high_concentration_soild=100
         		low_concentration=float(entry_main_construction.get())*0.55
         		high_concentration=float(entry_first_construction.get())
         		old_conversion=low_concentration
         		new_conversion=high_concentration
         		start_solution_weight=high_concentration_soild-new_conversion
         		start_soild_weight=abs(old_conversion-new_conversion)
         		end_solution_weight=float(entry_weight.get())
         		end_soild_weight=(start_soild_weight*end_solution_weight)/start_solution_weight
         		bombyx_conversion=new_conversion
         		solution_density=145/(145-bombyx_conversion)
         		finally_solution_weight=end_solution_weight+end_soild_weight
         		solution_volume=finally_solution_weight/solution_density
         	elif var_soulation_type.get() =="Salad" and var_construction_type_main.get()=="Balng" and var_construction_type_first.get() =="Salometer":
         		type="Bomiat"
         		high_concentration_soild=100
         		low_concentration=float(entry_main_construction.get())*0.55
         		high_concentration=float(entry_first_construction.get())/4
         		old_conversion=low_concentration
         		new_conversion=high_concentration
         		start_solution_weight=high_concentration_soild-new_conversion
         		start_soild_weight=abs(old_conversion-new_conversion)
         		end_solution_weight=float(entry_weight.get())
         		end_soild_weight=(start_soild_weight*end_solution_weight)/start_solution_weight
         		bombyx_conversion=new_conversion
         		solution_density=145/(145-bombyx_conversion)
         		finally_solution_weight=end_solution_weight+end_soild_weight
         		solution_volume=finally_solution_weight/solution_density
         	elif var_soulation_type.get() =="Salad" and var_construction_type_main.get()=="Salometer" and var_construction_type_first.get() =="Salometer":
         		type="Bomiat"
         		high_concentration_soild=100
         		low_concentration=float(entry_main_construction.get())/4
         		high_concentration=float(entry_first_construction.get())/4
         		old_conversion=low_concentration
         		new_conversion=high_concentration
         		start_solution_weight=high_concentration_soild-new_conversion
         		start_soild_weight=abs(old_conversion-new_conversion)
         		end_solution_weight=float(entry_weight.get())
         		end_soild_weight=(start_soild_weight*end_solution_weight)/start_solution_weight
         		bombyx_conversion=new_conversion
         		solution_density=145/(145-bombyx_conversion)
         		finally_solution_weight=end_solution_weight+end_soild_weight
         		solution_volume=finally_solution_weight/solution_density
         	elif var_soulation_type.get() =="Salad" and var_construction_type_main.get()=="Salometer" and var_construction_type_first.get() =="Bomiat":
         		type="Bomiat"
         		high_concentration_soild=100
         		low_concentration=float(entry_main_construction.get())/4
         		high_concentration=float(entry_first_construction.get())
         		old_conversion=low_concentration
         		new_conversion=high_concentration
         		start_solution_weight=high_concentration_soild-new_conversion
         		start_soild_weight=abs(old_conversion-new_conversion)
         		end_solution_weight=float(entry_weight.get())
         		end_soild_weight=(start_soild_weight*end_solution_weight)/start_solution_weight
         		bombyx_conversion=new_conversion
         		solution_density=145/(145-bombyx_conversion)
         		finally_solution_weight=end_solution_weight+end_soild_weight
         		solution_volume=finally_solution_weight/solution_density
         	elif var_soulation_type.get() =="Salad" and var_construction_type_main.get()=="Salometer" and var_construction_type_first.get() =="Balng":
         		type="Bomiat"
         		high_concentration_soild=100
         		low_concentration=float(entry_main_construction.get())/4
         		high_concentration=float(entry_first_construction.get())*0.55
         		old_conversion=low_concentration
         		new_conversion=high_concentration
         		start_solution_weight=high_concentration_soild-new_conversion
         		start_soild_weight=abs(old_conversion-new_conversion)
         		end_solution_weight=float(entry_weight.get())
         		end_soild_weight=(start_soild_weight*end_solution_weight)/start_solution_weight
         		bombyx_conversion=new_conversion
         		solution_density=145/(145-bombyx_conversion)
         		finally_solution_weight=end_solution_weight+end_soild_weight
         		solution_volume=finally_solution_weight/solution_density
             #if var_soulation_type.get()== "Salad":
#                 soulation_type=reshape("ملحى")[::-1]
                 #soul = reshape("كمية الملح اللازمة اضافتها لرفع تركيز المحلول")[::-1]
#                 construction_type=reshape("بومية")[::-1]
             #else:
#                 soulation_type=reshape("سكرى")[::-1]
#                 soul = reshape("كمية السكر اللازمة اضافتها لرفع تركيز المحلول")[::-1]
#                 construction_type=reshape("بالنج")[::-1]
         	if var_soulation_type.get()=="Salad":
         	    soulation_type=reshape("ملحى")[::-1]
         	    soul = reshape("كمية الملح اللازمة اضافتها لرفع تركيز المحلول")[::-1]
         	    construction_type=reshape("بومية")[::-1]
         	else:
         	    soulation_type=reshape("سكرى")[::-1]
         	    soul = reshape("كمية السكر اللازمة اضافتها لرفع تركيز المحلول")[::-1]
         	    construction_type=reshape("بالنج")[::-1]
         	label_result.config(text=f"{soulation_type} = {reshape('نوع المحلول المطلوب رفع تركيزه')[::-1]}\n{reshape('كجم')[::-1]} {end_solution_weight} = {reshape('وزن المحلول قبل رفع تركيزه')[::-1]}\n{construction_type} {old_conversion:.2f} = {reshape('التركيز القديم قبل الرفع')[::-1]}\n{construction_type} {new_conversion:.2f} = {reshape('التركيز الجديد بعد الرفع')[::-1]}\n{reshape('كجم')[::-1]} {end_soild_weight:.2f} = {soul}\n{reshape('كجم')[::-1]} {finally_solution_weight:.2f} = {reshape('الوزن النهائي للمحلول بعد رفع تركيزه')[::-1]}\n{reshape('لتر')[::-1]} {solution_volume:.2f} = {reshape('حجم المحلول بعد رفع تركيزه')[::-1]}\n{reshape('كجم/لتر')[::-1]} {solution_density:.2f} = {reshape('كثافة المحلول بعد رفع تركيزه')[::-1]}")
         		
         else:
            messagebox.showinfo("Cutton",reshape("من فضلك أدخل جميع البيانات")[::-1])
    elif var_opretor_type.get()=="Mixing":
         if len(entry_weight.get())>0 and len(entry_main_construction.get())>0 and len(entry_first_construction.get())>0 and len(entry_second_construction.get())>0 and var_soulation_type.get() in soulation_type_list and  var_construction_type_main.get() in construction_type_list and  var_construction_type_first.get() in construction_type_list and  var_construction_type_second.get() in construction_type_list:
             finally_concentration=float(entry_main_construction.get())
             first_concentration=float(entry_first_construction.get())
             second_concentration=float(entry_second_construction.get())
             if var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Balng" and var_construction_type_first.get() == "Balng" and var_construction_type_second.get() == "Balng":
                 type='Balng'
                 finally_conversion=finally_concentration
                 first_conversion=first_concentration
                 second_conversion=second_concentration
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Balng" and var_construction_type_first.get() == "Balng" and var_construction_type_second.get() == "Bomiat":
                 type='Balng'
                 finally_conversion=finally_concentration
                 first_conversion=first_concentration
                 second_conversion=second_concentration/0.55
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Balng" and var_construction_type_first.get() == "Balng" and var_construction_type_second.get() == "Salometer":
                 type='Balng'
                 finally_conversion=finally_concentration
                 first_conversion=first_concentration
                 second_conversion=second_concentration/2.2
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Balng" and var_construction_type_first.get() == "Bomiat" and var_construction_type_second.get() == "Bomiat":
                 type='Balng'
                 finally_conversion=finally_concentration
                 first_conversion=first_concentration/0.55
                 second_conversion=second_concentration/0.55
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Balng" and var_construction_type_first.get() == "Bomiat" and var_construction_type_second.get() == "Balng":
                 type='Balng'
                 finally_conversion=finally_concentration
                 first_conversion=first_concentration/0.55
                 second_conversion=second_concentration
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Balng" and var_construction_type_first.get() == "Bomiat" and var_construction_type_second.get() == "Salometer":
                 type='Balng'
                 finally_conversion=finally_concentration
                 first_conversion=first_concentration/0.55
                 second_conversion=second_concentration/2.2
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Balng" and var_construction_type_first.get() == "Salometer" and var_construction_type_second.get() == "Salometer":
                 type='Balng'
                 finally_conversion=finally_concentration
                 first_conversion=first_concentration/2.2
                 second_conversion=second_concentration/2.2
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Balng" and var_construction_type_first.get() == "Salometer" and var_construction_type_second.get() == "Balng":
                 type='Balng'
                 finally_conversion=finally_concentration
                 first_conversion=first_concentration/2.2
                 second_conversion=second_concentration
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Balng" and var_construction_type_first.get() == "Salometer" and var_construction_type_second.get() == "Bomiat":
                 type='Balng'
                 finally_conversion=finally_concentration
                 first_conversion=first_concentration/2.2
                 second_conversion=second_concentration*0.55
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Bomiat" and var_construction_type_first.get() == "Bomiat" and var_construction_type_second.get() == "Bomiat":
                 type='Balng'
                 finally_conversion=finally_concentration/0.55
                 first_conversion=first_concentration/0.55
                 second_conversion=second_concentration/0.55
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Bomiat" and var_construction_type_first.get() == "Bomiat" and var_construction_type_second.get() == "Balng":
                 type='Balng'
                 finally_conversion=finally_concentration/0.55
                 first_conversion=first_concentration/0.55
                 second_conversion=second_concentration
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Bomiat" and var_construction_type_first.get() == "Bomiat" and var_construction_type_second.get() == "Salometer":
                 type='Balng'
                 finally_conversion=finally_concentration/0.55
                 first_conversion=first_concentration/0.55
                 second_conversion=second_concentration/2.2
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Bomiat" and var_construction_type_first.get() == "Balng" and var_construction_type_second.get() == "Balng":
                 type='Balng'
                 finally_conversion=finally_concentration/0.55
                 first_conversion=first_concentration
                 second_conversion=second_concentration
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Bomiat" and var_construction_type_first.get() == "Balng" and var_construction_type_second.get() == "Bomiat":
                 type='Balng'
                 finally_conversion=finally_concentration/0.55
                 first_conversion=first_concentration
                 second_conversion=second_concentration/0.55
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Bomiat" and var_construction_type_first.get() == "Balng" and var_construction_type_second.get() == "Salometer":
                 type='Balng'
                 finally_conversion=finally_concentration/0.55
                 first_conversion=first_concentration
                 second_conversion=second_concentration/2.2
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Bomiat" and var_construction_type_first.get() == "Salometer" and var_construction_type_second.get() == "Salometer":
                 type='Balng'
                 finally_conversion=finally_concentration/0.55
                 first_conversion=first_concentration/2.2
                 second_conversion=second_concentration/2.2
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Bomiat" and var_construction_type_first.get() == "Salometer" and var_construction_type_second.get() == "Balng":
                 type='Balng'
                 finally_conversion=finally_concentration/0.55
                 first_conversion=first_concentration/2.2
                 second_conversion=second_concentration
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Bomiat" and var_construction_type_first.get() == "Salometer" and var_construction_type_second.get() == "Bomiat":
                 type='Balng'
                 finally_conversion=finally_concentration/0.55
                 first_conversion=first_concentration/2.2
                 second_conversion=second_concentration/0.55
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Salometer" and var_construction_type_first.get() == "Bomiat" and var_construction_type_second.get() == "Bomiat":
                 type='Balng'
                 finally_conversion=finally_concentration/2.2
                 first_conversion=first_concentration/0.55
                 second_conversion=second_concentration/0.55
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Salometer" and var_construction_type_first.get() == "Bomiat" and var_construction_type_second.get() == "Balng":
                 type='Balng'
                 finally_conversion=finally_concentration/2.2
                 first_conversion=first_concentration/0.55
                 second_conversion=second_concentration
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Salometer" and var_construction_type_first.get() == "Bomiat" and var_construction_type_second.get() == "Salometer":
                 type='Balng'
                 finally_conversion=finally_concentration/2.2
                 first_conversion=first_concentration/0.55
                 second_conversion=second_concentration/2.2
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Salometer" and var_construction_type_first.get() == "Balng" and var_construction_type_second.get() == "Bomiat":
                 type='Balng'
                 finally_conversion=finally_concentration/2.2
                 first_conversion=first_concentration
                 second_conversion=second_concentration/0.55
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Salometer" and var_construction_type_first.get() == "Balng" and var_construction_type_second.get() == "Balng":
                 type='Balng'
                 finally_conversion=finally_concentration/2.2
                 first_conversion=first_concentration
                 second_conversion=second_concentration
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Salometer" and var_construction_type_first.get() == "Balng" and var_construction_type_second.get() == "Salometer":
                 type='Balng'
                 finally_conversion=finally_concentration/2.2
                 first_conversion=first_concentration
                 second_conversion=second_concentration/2.2
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Salometer" and var_construction_type_first.get() == "Salometer" and var_construction_type_second.get() == "Bomiat":
                 type='Balng'
                 finally_conversion=finally_concentration/2.2
                 first_conversion=first_concentration/2.2
                 second_conversion=second_concentration/0.55
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Salometer" and var_construction_type_first.get() == "Salometer" and var_construction_type_second.get() == "Balng":
                 type='Balng'
                 finally_conversion=finally_concentration/2.2
                 first_conversion=first_concentration/2.2
                 second_conversion=second_concentration
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Suggar" and var_construction_type_main.get() == "Salometer" and var_construction_type_first.get() == "Salometer" and var_construction_type_second.get() == "Salometer":
                 type='Balng'
                 finally_conversion=finally_concentration/2.2
                 first_conversion=first_concentration/2.2
                 second_conversion=second_concentration/2.2
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion*0.55
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Balng" and var_construction_type_first.get() == "Balng" and var_construction_type_second.get() == "Balng":
                 type="Bomiat"
                 finally_conversion=finally_concentration*0.55
                 first_conversion=first_concentration*0.55
                 second_conversion=second_concentration*0.55
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Balng" and var_construction_type_first.get() == "Balng" and var_construction_type_second.get() == "Bomiat":
                 type="Bomiat"
                 finally_conversion=finally_concentration*0.55
                 first_conversion=first_concentration*0.55
                 second_conversion=second_concentration
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Balng" and var_construction_type_first.get() == "Balng" and var_construction_type_second.get() == "Salometer":
                 type="Bomiat"
                 finally_conversion=finally_concentration*0.55
                 first_conversion=first_concentration*0.55
                 second_conversion=second_concentration/4
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Balng" and var_construction_type_first.get() == "Bomiat" and var_construction_type_second.get() == "Balng":
                 type="Bomiat"
                 finally_conversion=finally_concentration*0.55
                 first_conversion=first_concentration
                 second_conversion=second_concentration*0.55
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Balng" and var_construction_type_first.get() == "Bomiat" and var_construction_type_second.get() == "Bomiat":
                 type="Bomiat"
                 finally_conversion=finally_concentration*0.55
                 first_conversion=first_concentration
                 second_conversion=second_concentration
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Balng" and var_construction_type_first.get() == "Bomiat" and var_construction_type_second.get() == "Salometer":
                 type="Bomiat"
                 finally_conversion=finally_concentration*0.55
                 first_conversion=first_concentration
                 second_conversion=second_concentration/4
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Balng" and var_construction_type_first.get() == "Salometer" and var_construction_type_second.get() == "Balng":
                 type="Bomiat"
                 finally_conversion=finally_concentration*0.55
                 first_conversion=first_concentration/4
                 second_conversion=second_concentration*0.55
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Balng" and var_construction_type_first.get() == "Salometer" and var_construction_type_second.get() == "Bomiat":
                 type="Bomiat"
                 finally_conversion=finally_concentration*0.55
                 first_conversion=first_concentration/4
                 second_conversion=second_concentration
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Balng" and var_construction_type_first.get() == "Salometer" and var_construction_type_second.get() == "Salometer":
                 type="Bomiat"
                 finally_conversion=finally_concentration*0.55
                 first_conversion=first_concentration/4
                 second_conversion=second_concentration/4
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                     ########
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Bomiat" and var_construction_type_first.get() == "Balng" and var_construction_type_second.get() == "Balng":
                 type="Bomiat"
                 finally_conversion=finally_concentration
                 first_conversion=first_concentration*0.55
                 second_conversion=second_concentration*0.55
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Bomiat" and var_construction_type_first.get() == "Balng" and var_construction_type_second.get() == "Bomiat":
                 type="Bomiat"
                 finally_conversion=finally_concentration
                 first_conversion=first_concentration*0.55
                 second_conversion=second_concentration
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Bomiat" and var_construction_type_first.get() == "Balng" and var_construction_type_second.get() == "Salometer":
                 type="Bomiat"
                 finally_conversion=finally_concentration
                 first_conversion=first_concentration*0.55
                 second_conversion=second_concentration/4
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Bomiat" and var_construction_type_first.get() == "Bomiat" and var_construction_type_second.get() == "Balng":
                 type="Bomiat"
                 finally_conversion=finally_concentration
                 first_conversion=first_concentration
                 second_conversion=second_concentration*0.55
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Bomiat" and var_construction_type_first.get() == "Bomiat" and var_construction_type_second.get() == "Bomiat":
                 type="Bomiat"
                 finally_conversion=finally_concentration
                 first_conversion=first_concentration
                 second_conversion=second_concentration
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Bomiat" and var_construction_type_first.get() == "Bomiat" and var_construction_type_second.get() == "Salometer":
                 type="Bomiat"
                 finally_conversion=finally_concentration
                 first_conversion=first_concentration
                 second_conversion=second_concentration/4
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Bomiat" and var_construction_type_first.get() == "Salometer" and var_construction_type_second.get() == "Balng":
                 type="Bomiat"
                 finally_conversion=finally_concentration
                 first_conversion=first_concentration/4
                 second_conversion=second_concentration*0.55
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Bomiat" and var_construction_type_first.get() == "Salometer" and var_construction_type_second.get() == "Bomiat":
                 type="Bomiat"
                 finally_conversion=finally_concentration
                 first_conversion=first_concentration/4
                 second_conversion=second_concentration
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Bomiat" and var_construction_type_first.get() == "Salometer" and var_construction_type_second.get() == "Salometer":
                 type="Bomiat"
                 finally_conversion=finally_concentration
                 first_conversion=first_concentration/4
                 second_conversion=second_concentration/4
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                     ####
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Salometer" and var_construction_type_first.get() == "Balng" and var_construction_type_second.get() == "Balng":
                 type="Bomiat"
                 finally_conversion=finally_concentration/4
                 first_conversion=first_concentration*0.55
                 second_conversion=second_concentration*0.55
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Salometer" and var_construction_type_first.get() == "Balng" and var_construction_type_second.get() == "Bomiat":
                 type="Bomiat"
                 finally_conversion=finally_concentration/4
                 first_conversion=first_concentration*0.55
                 second_conversion=second_concentration
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Salometer" and var_construction_type_first.get() == "Balng" and var_construction_type_second.get() == "Salometer":
                 type="Bomiat"
                 finally_conversion=finally_concentration/4
                 first_conversion=first_concentration*0.55
                 second_conversion=second_concentration/4
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Salometer" and var_construction_type_first.get() == "Bomiat" and var_construction_type_second.get() == "Balng":
                 type="Bomiat"
                 finally_conversion=finally_concentration/4
                 first_conversion=first_concentration
                 second_conversion=second_concentration*0.55
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Salometer" and var_construction_type_first.get() == "Bomiat" and var_construction_type_second.get() == "Bomiat":
                 type="Bomiat"
                 finally_conversion=finally_concentration/4
                 first_conversion=first_concentration
                 second_conversion=second_concentration
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Salometer" and var_construction_type_first.get() == "Bomiat" and var_construction_type_second.get() == "Salometer":
                 type="Bomiat"
                 finally_conversion=finally_concentration/4
                 first_conversion=first_concentration
                 second_conversion=second_concentration/4
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Salometer" and var_construction_type_first.get() == "Salometer" and var_construction_type_second.get() == "Balng":
                 type="Bomiat"
                 finally_conversion=finally_concentration/4
                 first_conversion=first_concentration/4
                 second_conversion=second_concentration*0.55
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Salometer" and var_construction_type_first.get() == "Salometer" and var_construction_type_second.get() == "Bomiat":
                 type="Bomiat"
                 finally_conversion=finally_concentration/4
                 first_conversion=first_concentration/4
                 second_conversion=second_concentration
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversioln
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             elif var_soulation_type.get() == "Salad" and var_construction_type_main.get() == "Salometer" and var_construction_type_first.get() == "Salometer" and var_construction_type_second.get() == "Salometer":
                 type="Bomiat"
                 finally_conversion=finally_concentration/4
                 first_conversion=first_concentration/4
                 second_conversion=second_concentration/4
                 if first_conversion>second_conversion:
                 	high_solution_wight=abs(first_conversion-finally_conversion)
                 	low_solution_wight=abs(second_conversion-finally_conversion)
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_entry=high_solution_wight+low_solution_wight
                 	soulation_wight_exit=float(entry_weight.get())
                 	high_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	low_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                 	bombyx_conversion=finally_conversion
                 	solution_density=145/(145-bombyx_conversion)
                 	solution_volume=soulation_wight_exit/solution_density
                 elif first_conversion<second_conversion:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
                 else:
                     high_solution_wight=abs(second_conversion-finally_conversion)
                     low_solution_wight=abs(first_conversion-finally_conversion)
                     soulation_wight_entry=high_solution_wight+low_solution_wight
                     soulation_wight_exit=float(entry_weight.get())
                     high_solution_wight_exit=(high_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     low_solution_wight_exit=(low_solution_wight*soulation_wight_exit)/soulation_wight_entry
                     bombyx_conversion=finally_conversion*0.55
                     solution_density=145/(145-bombyx_conversion)
                     solution_volume=soulation_wight_exit/solution_density
             if var_soulation_type.get()=="Salad":
                 soulation_type=reshape("ملحى")[::-1]
                 soul = reshape("كمية الملح اللازمة اضافتها لرفع تركيز المحلول")[::-1]
                 construction_type=reshape("بومية")[::-1]
             else:
                  soulation_type=reshape("سكرى")[::-1]
                  soul = reshape("كمية السكر اللازمة اضافتها لرفع تركيز المحلول")[::-1]
                  construction_type=reshape("بالنج")[::-1]
             label_result.config(text=f"{soulation_type} = {reshape('نوع المحلول المطلوب تحضيره')[::-1]}\n{construction_type} = {reshape('نوع تركيز المحلول المطلوب تحضيره')[::-1]}\n{reshape('كجم')[::-1]} {entry_weight.get()} = {reshape('وزن المحلول المطلوب تحضيره')[::-1]}\n{construction_type} {finally_conversion:.2f} = {reshape('تركيز المحلول المطلوب تحضيره')[::-1]}\n{reshape('كجم')[::-1]} {high_solution_wight_exit:.2f} = {construction_type} ({first_conversion:.2f}) {reshape('كمية المحلول اللازم اضافتها من المحلول')[::-1]}\n{reshape('كجم')[::-1]} {low_solution_wight_exit:.2f} = {construction_type} ({second_conversion:.2f}) {reshape('كمية المحلول اللازم اضافتها من المحلول')[::-1]}\n{reshape('لتر')[::-1]} {solution_volume:.2f} = {reshape('حجم المحلول')[::-1]}\n{reshape('كجم/لتر')[::-1]} {solution_density:.2f} = {reshape('كثافة المحلول')[::-1]}")
         else:
    	     messagebox.showinfo("Cutton",reshape("من فضلك أدخل جميع البيانات")[::-1])
label_main_title=Label(
                                         pro,
                                         text=reshape("هذا البرنامج تم إنشائه بواسطة مهندس محمد فايز")[::-1],
                                         font=("Arial",8,"bold"),
                                         bg="#E6A5FF",
                                         fg="green",
                                         relief="raised",
                                         bd=5
                                         )
label_main_title.place(x=1,y=1,width=680)
label_opretor_type=Label(
                                              pro,
                                              text=reshape("أختر نوع العملية")[::-1],
                                              font=("Arial",8,"bold"),
                                              bg="#FFE0E0",
                                              fg="black",
                                              relief="raised",
                                              bd=8
                                              )
label_opretor_type.place(x=1,y=350,width=680)
xx=1
count = 0
text_opretor = ["تحضير","خفض","رفع","خلط"]
for opretor in opretor_type_list:
	#راديو بوتون نوع العملية (ثابت)
	opretor_type=Radiobutton(
	                                                pro,
	                                                text=reshape(text_opretor[::-1][count])[::-1],
	                                                value=opretor,
	                                                font=("Arial",7,"bold"),
	                                                variable=var_opretor_type,
	                                                indicatoron=False,
	                                                selectcolor="green",
	                                                bg="#CC005E",
	                                                relief="raised",
	                                                bd=5,
	                                                command=placeing
	                                                )
	opretor_type.place(x=xx,y=408,width=170)
	xx+=170
	count+=1
label_soulation_type = Label(
                                                     pro,
                                                     text=reshape("أختر نوع المحلول")[::-1],
                                                     font=("Arial",8,"bold"),
                                                     bg="#FFE0E0",
                                                     fg="black",
                                                     relief="raised",
                                                     bd=8
                                                     )
label_soulation_type.place(x=1,y=463,width=680)
xx=1
count = 0
text_opretor = ["ملحي","سكرى"]
for soulation in soulation_type_list:
	soulation_type=Radiobutton(
	                                                   pro,
	                                                   text=reshape(text_opretor[count])[::-1],
	                                                   value=soulation,
	                                                   font=("Arial",8,"bold"),
	                                                   variable=var_soulation_type,
	                                                   relief="raised",
	                                                   bd=5,
	                                                   indicatoron=False,
	                                                   selectcolor="#E6FF70",
	                                                   activeforeground="blue",
	                                                   bg="#FF6564"
	                                                   )
	soulation_type.place(x=xx,y=517,width=340)
	xx+=340
	count+=1
label_entry_weight=Label(
                                              pro,
                                              text=reshape("وزن المحلول")[::-1],
                                              font=("Arial",7,"bold"),
                                              fg="lightblue",
                                              bg="#FF6564",
                                              relief="raised",
                                              bd=5
                                              )
label_entry_weight.place(x=1,y=50,width=325,height=50)
entry_weight=Entry(
                                    pro,
                                    fg="red",
                                    bg="#FFE0E0",
                                    relief="raised",
                                    bd=5
                                    )
entry_weight.place(x=330,y=50,width=345,height=50)
label_entry_main_construction=Label(
                                              pro,
                                              fg="lightblue",
                                              font=("Arial",7,"bold"),
                                              bg="#FF6564",
                                              relief="raised",
                                              bd=5
                                              )
label_entry_main_construction.place(x=1,y=120,width=325,height=50)
entry_main_construction=Entry(
                                    pro,
                                    fg="red",
                                    bg="#FFE0E0",
                                    relief="raised",
                                    bd=5
                                    )
entry_main_construction.place(x=330,y=120,width=345,height=50)
label_entry_first_construction=Label(
                                              pro,
                                              fg="lightblue",
                                              bg="#FF6564",
                                              font=("Arial",7,"bold"),
                                              relief="raised",
                                              bd=5
                                              )
entry_first_construction=Entry(
                                    pro,
                                    fg="red",
                                    bg="#FFE0E0",
                                    relief="raised",
                                    bd=5
                                    )
label_entry_second_construction=Label(
                                              pro,
                                              fg="lightblue",
                                              font=("Arial",7,"bold"),
                                              bg="#FF6564",
                                              relief="raised",
                                              bd=5
                                              )
entry_second_construction=Entry(
                                    pro,
                                    fg="red",
                                    bg="#FFE0E0",
                                    relief="raised",
                                    bd=5
                                    )
label_main_construction_type=Label(
                                                     pro,
                                                     font=("Arial",8,"bold"),
                                                     bg="#FFE0E0",
                                                     relief="raised",
                                                     bd=8
                                                     )
label_main_construction_type.place(x=1,y=570,width=680)
construction_type_balng_main=Radiobutton(
                                                                          pro,
                                                                          text=reshape("بالنج")[::-1],
                                                                          value="Balng",
                                                                          font=("Arial",8,"bold"),
                                                                          variable=var_construction_type_main,
                                                                          indicatoron=False,
                                                                          relief="raised",
                                                                          bd=6,
                                                                          selectcolor="#E6FF70",
                                                                          bg="#FF6564"
                                                                        )
construction_type_balng_main.place(x=452,y=625,width=228)
construction_type_bomiat_main=Radiobutton(
                                                                          pro,
                                                                          text=reshape("بومية")[::-1],
                                                                          value="Bomiat",
                                                                          font=("Arial",8,"bold"),
                                                                          variable=var_construction_type_main,
                                                                          indicatoron=False,
                                                                          relief="raised",
                                                                          bd=6,
                                                                          selectcolor="#E6FF70",
                                                                          bg="#FF6564"
                                                                        )
construction_type_bomiat_main.place(x=226,y=625,width=226)
construction_type_salometer_main=Radiobutton(
                                                                          pro,
                                                                          text=reshape("سالومتر")[::-1],
                                                                          value="Salometer",
                                                                          font=("Arial",8,"bold"),
                                                                          variable=var_construction_type_main,
                                                                          indicatoron=False,
                                                                          relief="raised",
                                                                          bd=6,
                                                                          selectcolor="#E6FF70",
                                                                          bg="#FF6564"
                                                                        )
construction_type_salometer_main.place(x=1,y=625,width=226)
#######
label_first_construction_type=Label(
                                                     pro,
                                                     font=("Arial",8,"bold"),
                                                     bg="#FFE0E0",
                                                     relief="raised",
                                                     bd=8
                                                     )
construction_type_balng_first=Radiobutton(
                                                                          pro,
                                                                          text=reshape("بالنج")[::-1],
                                                                          value="Balng",
                                                                          font=("Arial",8,"bold"),
                                                                          variable=var_construction_type_first,
                                                                          indicatoron=False,
                                                                          relief="raised",
                                                                          bd=6,
                                                                          selectcolor="#E6FF70",
                                                                          bg="#FF6564"
                                                                        )
construction_type_bomiat_first=Radiobutton(
                                                                          pro,
                                                                          text=reshape("بومية")[::-1],
                                                                          value="Bomiat",
                                                                          font=("Arial",8,"bold"),
                                                                          variable=var_construction_type_first,
                                                                          indicatoron=False,
                                                                          relief="raised",
                                                                          bd=6,
                                                                          selectcolor="#E6FF70",
                                                                          bg="#FF6564"
                                                                        )
construction_type_salometer_first=Radiobutton(
                                                                          pro,
                                                                          text=reshape("سالومتر")[::-1],
                                                                          value="Salometer",
                                                                          font=("Arial",8,"bold"),
                                                                          variable=var_construction_type_first,
                                                                          indicatoron=False,
                                                                          relief="raised",
                                                                          bd=6,
                                                                          selectcolor="#E6FF70",
                                                                          bg="#FF6564"
                                                                        )
####$
label_second_construction_type=Label(
                                                     pro,
                                                     font=("Arial",8,"bold"),
                                                     bg="#FFE0E0",
                                                     relief="raised",
                                                     bd=8
                                                     )
construction_type_balng_second=Radiobutton(
                                                                          pro,
                                                                          text=reshape("بالنج")[::-1],
                                                                          value="Balng",
                                                                          font=("Arial",8,"bold"),
                                                                          variable=var_construction_type_second,
                                                                          indicatoron=False,
                                                                          relief="raised",
                                                                          bd=6,
                                                                          selectcolor="#E6FF70",
                                                                          bg="#FF6564"
                                                                        )
construction_type_bomiat_second=Radiobutton(
                                                                          pro,
                                                                          text=reshape("بومية")[::-1],
                                                                          value="Bomiat",
                                                                          font=("Arial",8,"bold"),
                                                                          variable=var_construction_type_second,
                                                                          indicatoron=False,
                                                                          relief="raised",
                                                                          bd=6,
                                                                          selectcolor="#E6FF70",
                                                                          bg="#FF6564"
                                                                        )
construction_type_salometer_second=Radiobutton(
                                                                          pro,
                                                                          text=reshape("سالومتر")[::-1],
                                                                          value="Salometer",
                                                                          font=("Arial",8,"bold"),
                                                                          variable=var_construction_type_second,
                                                                          indicatoron=False,
                                                                          relief="raised",
                                                                          bd=6,
                                                                          selectcolor="#E6FF70",
                                                                          bg="#FF6564"
                                                                        )
calculate_button=Button(
                                             pro,
                                             text=reshape("عرض النتيجة")[::-1],
                                             font=("Arial",8,"bold"),
                                             bg="#E00079",
                                             fg="lightblue",
                                             relief="raised",
                                             activebackground="lightblue",
                                             activeforeground="blue",
                                             bd=8,
                                             command=culculate,
                                             padx=5,
                                             pady=60
                                             )
label_result_result=Label(
                                             pro,
                                             text=reshape("النتيجة")[::-1],
                                             font=("Arial",8,"bold"),
                                             relief="raised",
                                             bd=6,
                                             bg="#C8C8A7"
                                             )
label_result_result.place(x=1,y=990,width=680)
label_result=Label(
                                 pro,
                                 bg="#760025",
                                 fg="#23FF00",
                                 anchor="n",
                                 font=("Arial",6,"bold"),
                                 padx=2,
                                 relief="sunken",
                                 bd=2,
                                 
                                 )
label_result.place(x=1,y=1040,width=680,height=1480-964)
placeing()
pro.mainloop()