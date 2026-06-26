from flask import Flask, redirect,render_template,request, url_for 
from class_test import tabledb
import os 
import sqlite3
import datetime as dt 



# rute database file
databasename = os.getcwd() + '/tes.db'



app = Flask(__name__)


@app.route('/')
def home():
  return f'''
  <!DOCTYPE html> 
  <html lang="en">
    <head>
      <title>Welcome</title>
      <style>
        * {{
          margin: 0;
          padding: 0;
          box-sizing: border-box;
        }}
        body {{
          background-color: #ffffff;
          font-family: 'Segoe UI', sans-serif;
          color: #333;
          display: flex;
          flex-direction: column;
          min-height: 100vh;
        }}
        .flying-navigation-button {{
          position: fixed;
          top: 0;
          left: 0;
          width: 100%;
          background-color: #f8f8f8;
          border-bottom: 1px solid #ddd;
          padding: 12px 20px;
          z-index: 999;
          display: flex;
          justify-content: flex-start;
          box-shadow: 0 2px 4px rgba(0,0,0,0.03);
        }}
        .btn {{
          display: flex;
          gap: 30px;
        }}
        .btn a {{
          color: #333;
          text-decoration: none;
          font-size: 17px;
          font-weight: 500;
          padding: 6px 8px;
          border-bottom: 2px solid transparent;
          transition: all 0.2s ease;
        }}
        .btn a:hover {{
          border-bottom: 2px solid #333;
        }}
        .main-content {{
          flex: 1; 
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
          margin-top: 50px;
        }}
        .img img {{
          width: 200px;
          border-radius: 12px;
          border: 1px solid #ddd;
          box-shadow: 0 4px 8px rgba(0,0,0,0.08);
        }}
        .welcome {{
          text-align: center;
          margin-top: 16px;
        }}
        .welcome h1 {{
          font-size: 32px;
          color: #222;
          letter-spacing: 2px;
        }}
        footer {{
          background-color: #f8f8f8;
          border-top: 1px solid #ddd;
          padding: 24px 20px;
          text-align: center;
        }}
        .footer-content {{
          display: flex;
          flex-direction: column;
          align-items: center;
          gap: 12px;
        }}
        .footer-content > a {{
          color: #555;
          text-decoration: none;
          font-size: 14px;
          transition: color 0.2s ease;
        }}
        .footer-content > a:hover {{
          color: #000;
          text-decoration: underline;
        }}
        .social {{
          display: flex;
          gap: 16px;
          justify-content: center;
        }}
        .social a {{
          display: inline-block;
          transition: transform 0.2s ease;
        }}
        .social a:hover {{
          transform: scale(1.15);
        }}
        .social img {{
          width: 26px;
          height: 26px;
          filter: grayscale(100%);
          transition: filter 0.2s ease;
        }}
        .social a:hover img {{
          filter: grayscale(0%);
        }}
        .copyright p {{
          font-size: 13px;
          color: #888;
          margin-top: 4px;
        }}
      </style>
    </head>
    <body>
      <div class="flying-navigation-button">
        <div class="btn">
          <a href="{url_for('index')}">Db result</a>
          <a href="{url_for('tambah')}">Input</a>
        </div> 
      </div>

      <div class="main-content">
        <div class="img">
          <img src="{url_for('static', filename='bochi.jpg')}" alt="ss">
        </div>
        <div class="welcome">
          <marquee><h1>{dt.date.today()}</h1></marquee>
        </div>
      </div>

      <footer id="footer">
        <div class="footer-content">
          <a href="mailto:mraditradit808@gmail.com">mraditradit808@gmail.com</a>
          <div class="social">
            <a href="https://github.com/Raditya808" target="_blank">
              <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="Github">
            </a>
            <a href="https://www.instagram.com/4ku_raditya/" target="_blank">
              <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="Instagram">
            </a>
            <a href="https://www.facebook.com/yourprofile" target="_blank">
              <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="Facebook">
            </a>
          </div>
          <div class="copyright">
            <p>Copyright &copy; 2025 Raditya. All rights reserved</p>
          </div>
        </div>
      </footer>
    </body>
  </html> 
  '''


@app.route('/home')
def index():
    conn = sqlite3.connect(databasename)
    cursor = conn.cursor() 
    container = []
    for nomor,nama,harga in cursor.execute('SELECT * FROM dbtes'):
        model = tabledb(nomor,nama,harga)
        container.append(model)
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('index.html',container=container)


@app.route('/tambah',methods=['GET','POST'])
def tambah():
    if request.method =='POST':
        nomor = int(request.form['nomor'])
        nama = request.form['nama']
        harga = int(request.form['harga'])
        model = tabledb(nomor,nama,harga)
        model.tambah()
        return redirect(url_for('index'))
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Tambah</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
               * {{ margin: 0; padding: 0; box-sizing: border-box; }}

                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: #ffffff; /* Ubah ke putih */
                    color: #333; /* Warna teks gelap */
                    min-height: 100vh;
                    padding: 40px 20px;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    animation: fadeIn 0.8s ease-out;
                }}

               
                h1 {{
                    text-align: center;
                    color: #222; /* Warna judul gelap */
                    font-size: 2.5rem;
                    margin-bottom: 40px;
                    font-weight: 300;
                    letter-spacing: 2px;
                    animation: fadeInDown 0.8s ease;
                }}

               
                form {{
                    background: #ffffff;
                    padding: 40px;
                    border-radius: 8px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.05); /* Shadow lebih halus */
                    max-width: 500px;
                    width: 100%;
                    animation: fadeInUp 1s ease;
                    border: 1px solid #eee; /* Border tipis */
                }}

            

                input[type="number"],
                input[type="text"] {{
                    width: 100%;
                    padding: 15px 20px;
                    margin-bottom: 20px;
                    border: 1px solid #ddd; /* Border input abu */
                    border-radius: 6px;
                    font-size: 1rem;
                    color: #333;
                    transition: all 0.3s ease;
                }}

                input[type="number"]:focus,
                input[type="text"]:focus {{
                    outline: none;
                    border-color: #333; /* Fokus gelap */
                    box-shadow: 0 0 0 3px rgba(0,0,0,0.05);
                }}

                input[type="submit"] {{
                    width: 100%;
                    padding: 15px 20px;
                    background: #333; /* Tombol gelap */
                    color: white;
                    border: none;
                    border-radius: 6px;
                    font-size: 1rem;
                    font-weight: 500;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                }}

                input[type="submit"]:hover {{
                    background: #555;
                }}

                .nav-back {{
                    margin-top: 25px;
                }}

                .nav-back a {{
                    display: inline-block;
                    padding: 12px 28px;
                    background: transparent;
                    color: #333;
                    text-decoration: none;
                    border: 1px solid #333;
                    border-radius: 6px;
                    font-weight: 500;
                    transition: all 0.3s ease;
                }}

                .nav-back a:hover {{
                    background: #333;
                    color: white;
                }}

                footer {{
                    margin-top: 40px;
                    font-size: 0.9rem;
                    color: #888; /* Footer abu */
                    text-align: center;
                }}
            </style>
        </head>
        <body>
            <h1>Tambah Data</h1>
            <form method='POST'>
                <input type="number" name="nomor" placeholder="Masukkan nomor" required>
                <input type="text" name="nama" placeholder="Masukkan nama" required>
                <input type="number" name="harga" placeholder="Masukkan harga" required>
                <input type="submit" value="Kirim Data">
            </form>
            
            <div class="nav-back">
                <a href="{url_for('index')}">← Kembali</a>
            </div>

            <footer>
                <p>Utamakan Input Nomor yang Belum Ada untuk Menghindari Konflik Data.</p>
            </footer>
        </body>
    </html>
"""
@app.route('/ubah/<int:id>',methods=['GET','POST'])
def ubah(id):
    model = tabledb()
    model.load(id)
    if request.method=='POST':
        nomor = int(request.form['nomor'])
        nama = request.form['nama']
        harga = int(request.form['harga'])
        model = tabledb(nomor,nama,harga)
        model.ubah()
        return redirect(url_for('index'))
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>Ubah</title>
       <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}

            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: #ffffff; /* Warna background bersih */
                min-height: 100vh;
                padding: 40px 20px;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }}

            h1 {{
                text-align: center;
                color: #222; /* Judul gelap */
                font-size: 2.5rem;
                margin-bottom: 40px;
                font-weight: 300;
                letter-spacing: 2px;
            }}

            form {{
                background: white;
                padding: 40px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.05); /* Shadow halus */
                max-width: 500px;
                width: 100%;
                border: 1px solid #eee;
            }}

            input[type="number"],
            input[type="text"] {{
                width: 100%;
                padding: 15px 20px;
                margin-bottom: 20px;
                border: 1px solid #ddd;
                border-radius: 6px;
                font-size: 1rem;
                color: #333;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}

            input[type="number"]:focus,
            input[type="text"]:focus {{
                outline: none;
                border-color: #333;
            }}

            input[type="submit"] {{
                width: 100%;
                padding: 15px 20px;
                background: #333; /* Warna tombol gelap */
                color: white;
                border: none;
                border-radius: 6px;
                font-size: 1rem;
                font-weight: 500;
                cursor: pointer;
            }}

            input[type="submit"]:hover {{
                background: #555;
            }}

            button {{
                margin-top: 20px;
                padding: 0;
                background: white;
                border: 1px solid #ddd;
                border-radius: 6px;
                cursor: pointer;
            }}

            button:hover {{
                background: #f8f8f8;
            }}

            button a {{
                display: block;
                padding: 12px 28px;
                color: #333;
                text-decoration: none;
                font-weight: 500;
                font-size: 0.95rem;
            }}

            footer {{
                margin-top: 40px;
                font-size: 0.9rem;
                color: #888;
                text-align: center;
            }}
        </style>  
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
    <h1>Ubah</h1>
     <form method='POST'>  
        <input type='number' name='nomor' placeholder='masukan nomor sesuai isi tabel'><br>
        <input type="text" name="nama" placeholder="masukan nama yang ingin diganti"><br>
        <input type="number" name="harga" placeholder="masukan harga yang ingin diganti"><br>
        <input type="submit" value="kirim"><br> 
    </form> 
     <button>
        <a href="{url_for('index')}">Kembali</a>
        </button>
        <br>
        
        <footer>
        <p>Utamakan Input Nomor Yang Sesuai Isi Tabel Sebelum Nya</p>
        </footer>
    </html>
    </body>
    """

# hapus 
@app.route('/hapusdata/<int:id>')
def hapus(id):
   model = tabledb()
   model.load(id)
   model.hapus()
   return redirect(url_for('index'))
   


if __name__=="__main__":
    app.run(debug=True)
