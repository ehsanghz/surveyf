# import tkinter as tk
# from tkinter import messagebox, Toplevel
# from pymongo import MongoClient
# from pymongo.errors import ConnectionFailure
# from PIL import Image, ImageTk
# import pandas as pd
# import jdatetime  # For Jalali (Persian) date conversion
# from datetime import datetime

# # Connect to MongoDB
# def connect_to_mongodb():
#     try:
#         uri = "mongodb+srv://pteline:Pass123123@pteline.xpzcd.mongodb.net/?retryWrites=true&w=majority&appName=pteline"
#         client = MongoClient(uri)
#         client.admin.command('ping')  # Check connection
#         return client
#     except ConnectionFailure as e:
#         messagebox.showerror("Error", f"Failed to connect to MongoDB: {e}")
#         return None

# # Save data to MongoDB
# def save_to_mongodb(data):
#     client = connect_to_mongodb()
#     if client:
#         try:
#             db = client['survey_database']
#             collection = db['survey_results']
#             collection.insert_one({
#                 "نام و نام خانوادگی": data[0],
#                 "شماره تماس": data[1],
#                 "زبان‌آموز بوده": data[2],
#                 "نمره هدف": data[3],
#                 "نام استاد": data[4],
#                 "نمره دریافتی": data[5],
#                 "توضیحات": data[6],
#                 "تاریخ ذخیره‌سازی": data[7],
#                 "زمان ذخیره‌سازی": data[8]
#             })
#             messagebox.showinfo("Success", "Data saved successfully.")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to save data: {e}")
#         finally:
#             client.close()

# # Submit data
# def submit():
#     full_name = entry_full_name.get()
#     phone_number = entry_phone_number.get()
#     is_student = var_is_student.get()
#     target_score = entry_target_score.get()
#     teacher = entry_teacher.get()
#     received_score = entry_received_score.get()
#     description = text_description.get("1.0", tk.END)

#     # Get Jalali date and current time
#     jalali_date = jdatetime.date.today().strftime('%Y/%m/%d')
#     save_time = datetime.now().strftime('%H:%M:%S')

#     if full_name and phone_number and target_score and teacher and received_score:
#         data = [full_name, phone_number, is_student, target_score, teacher, received_score, description, jalali_date, save_time]
#         save_to_mongodb(data)
#     else:
#         messagebox.showerror("Error", "Please fill in all fields.")

# # Show data
# def show_data():
#     client = connect_to_mongodb()
#     if client:
#         try:
#             db = client['survey_database']
#             collection = db['survey_results']
#             results = collection.find()

#             data_str = "Stored Data:\n\n"
#             for result in results:
#                 data_str += f"نام و نام خانوادگی: {result['نام و نام خانوادگی']}, شماره تماس: {result['شماره تماس']}, زبان‌آموز بوده: {result['زبان‌آموز بوده']}, " \
#                              f"نمره هدف: {result['نمره هدف']}, نام استاد: {result['نام استاد']}, نمره دریافتی: {result['نمره دریافتی']}, توضیحات: {result['توضیحات']}, " \
#                              f"تاریخ ذخیره‌سازی: {result['تاریخ ذخیره‌سازی']}, زمان ذخیره‌سازی: {result['زمان ذخیره‌سازی']}\n"

#             messagebox.showinfo("Results", data_str)
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to retrieve data: {e}")
#         finally:
#             client.close()

# # Export data to Excel
# def export_to_excel():
#     client = connect_to_mongodb()
#     if client:
#         try:
#             db = client['survey_database']
#             collection = db['survey_results']
#             results = list(collection.find())

#             if results:
#                 df = pd.DataFrame(results)
#                 df = df.drop(columns=['_id'])
#                 df.to_excel("survey_results.xlsx", index=False)
#                 messagebox.showinfo("Success", "Data exported to Excel.")
#             else:
#                 messagebox.showinfo("Info", "No data to export.")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to export data: {e}")
#         finally:
#             client.close()

# # Delete all data
# def delete_all_data():
#     client = connect_to_mongodb()
#     if client:
#         try:
#             db = client['survey_database']
#             collection = db['survey_results']
#             collection.delete_many({})
#             messagebox.showinfo("Success", "All data deleted successfully.")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to delete data: {e}")
#         finally:
#             client.close()

# # Create the UI
# root = tk.Tk()
# root.title("Survey Form")
# root.geometry("500x600")

# # Form fields
# tk.Label(root, text="نام و نام خانوادگی:").place(x=50, y=120)
# entry_full_name = tk.Entry(root, width=30)
# entry_full_name.place(x=180, y=120)

# tk.Label(root, text="شماره تماس:").place(x=50, y=150)
# entry_phone_number = tk.Entry(root, width=30)
# entry_phone_number.place(x=180, y=150)

# tk.Label(root, text="زبان‌آموز بوده:").place(x=50, y=180)
# var_is_student = tk.StringVar(value="بله")
# tk.Radiobutton(root, text="بله", variable=var_is_student, value="بله").place(x=180, y=180)
# tk.Radiobutton(root, text="خیر", variable=var_is_student, value="خیر").place(x=230, y=180)

# tk.Label(root, text="نمره هدف:").place(x=50, y=210)
# entry_target_score = tk.Entry(root, width=30)
# entry_target_score.place(x=180, y=210)

# tk.Label(root, text="نام استاد:").place(x=50, y=240)
# entry_teacher = tk.Entry(root, width=30)
# entry_teacher.place(x=180, y=240)

# tk.Label(root, text="نمره دریافتی:").place(x=50, y=270)
# entry_received_score = tk.Entry(root, width=30)
# entry_received_score.place(x=180, y=270)

# tk.Label(root, text="توضیحات:").place(x=50, y=300)
# text_description = tk.Text(root, wrap=tk.WORD, width=35, height=5)
# text_description.place(x=180, y=300)

# # Buttons
# tk.Button(root, text="Submit", command=submit, width=15, height=2).place(x=100, y=420)
# tk.Button(root, text="Show Data", command=show_data, width=15, height=2).place(x=250, y=420)
# tk.Button(root, text="Export to Excel", command=export_to_excel, width=15, height=2).place(x=100, y=480)
# tk.Button(root, text="Delete All Data", command=delete_all_data, width=15, height=2).place(x=250, y=480)

# root.mainloop()



from flask import Flask, render_template, request, redirect, url_for, send_file
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import jdatetime
import qrcode
import os
import pandas as pd
from io import BytesIO

app = Flask(__name__)

# اتصال به MongoDB
def connect_to_mongodb():
    try:
        uri = "mongodb+srv://pteline:Pass123123@pteline.xpzcd.mongodb.net/?retryWrites=true&w=majority&appName=pteline"
        client = MongoClient(uri)
        client.admin.command('ping')
        return client
    except ConnectionFailure as e:
        print(f"Connection failed: {e}")
        return None

# مسیر ذخیره‌سازی QR کدها
qr_folder = "static/qr_codes"
if not os.path.exists(qr_folder):
    os.makedirs(qr_folder)

# صفحه اصلی فرم نظرسنجی
@app.route("/", methods=["GET", "POST"])
def survey_form():
    if request.method == "POST":
        data = {
            "نام و نام خانوادگی": request.form.get("fullname"),
            "شماره تماس": request.form.get("phone"),
            "توضیحات": request.form.get("feedback"),
            "زبان‌آموز PTELine": request.form.get("pteline_student"),
            "نام استاد": request.form.get("teacher_name"),
            "نمره هدف": request.form.get("target_score"),
            "نمره دریافتی": request.form.get("received_score"),
            "تاریخ و زمان ثبت": jdatetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        client = connect_to_mongodb()
        if client:
            db = client['survey_database']
            collection = db['survey_results']
            collection.insert_one(data)
            client.close()
        return redirect(url_for("thank_you"))
    return render_template("form.html")

# صفحه تشکر پس از ارسال فرم
@app.route("/thank-you")
def thank_you():
    return render_template("thank_you.html")

# تولید QR کد
@app.route("/generate-qr")
def generate_qr():
    url = request.url_root  # لینک اصلی سایت
    qr_img = qrcode.make(url)
    qr_path = os.path.join(qr_folder, "survey_qr.png")
    qr_img.save(qr_path)
    return f"<h1>QR کد با موفقیت تولید شد.</h1><br><img src='/static/qr_codes/survey_qr.png' alt='QR Code'/>"

# دانلود اطلاعات به‌صورت اکسل
@app.route("/download-excel")
def download_excel():
    client = connect_to_mongodb()
    if client:
        db = client['survey_database']
        collection = db['survey_results']
        data = list(collection.find({}, {'_id': 0}))  # حذف _id برای نمایش ساده‌تر
        client.close()

        # تبدیل داده‌ها به فایل اکسل
        df = pd.DataFrame(data)
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='SurveyData')
        output.seek(0)

        return send_file("survey_results.xlsx", as_attachment=True, download_name="survey_results.xlsx")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # یا پورت دیگری که در سرور قابل دسترسی است
