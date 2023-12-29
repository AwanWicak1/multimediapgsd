from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    judul = "Konten Website"
    return render_template('home.html', judul=judul)


@app.route('/capaian')
def cptp():
    judul = "Capaian Pembelajaran"
    judul2 = "Tujuan Pembelajaran"
    return render_template('cptp.html', judul=judul, judul2=judul2)


@app.route('/kumpulanmateri')
def kumpulan():
    judul = "Kumpulan Materi"
    return render_template('kumpulanmateri.html', judul=judul)


@app.route('/petakonsep')
def petakonsep():
    judul = "Peta Konsep"
    return render_template('petakonsep.html', judul=judul)


@app.route('/materiwujudbenda')
def materi1():
    judul = "3 Wujud Benda"
    subjudul1 = "Benda"
    subjudul2 = "Benda Padat"
    subjudul3 = "Benda Cair"
    subjudul4 = "Benda Gas"
    subjudul5 = "Referensi"
    return render_template('materi1.html', judul=judul, subjudul1=subjudul1, subjudul2=subjudul2, subjudul3=subjudul3, subjudul4=subjudul4, subjudul5=subjudul5)


@app.route('/materiperubahanwujudbenda')
def materi2():
    judul = "Perubahan Wujud Benda"
    subjudul1 = "6 Perubahan Wujud Benda"
    subjudul2 = "1. Membeku"
    subjudul3 = "2. Mencair"
    subjudul4 = "3. Menguap"
    subjudul5 = "4. Mengembun"
    subjudul6 = "5. Menyublim"
    subjudul7 = "6. Mengkristal"
    subjudul8 = "Referensi"
    return render_template('materi2.html', judul=judul, subjudul1=subjudul1, subjudul2=subjudul2, subjudul3=subjudul3, subjudul4=subjudul4, subjudul5=subjudul5, subjudul6=subjudul6, subjudul7=subjudul7, subjudul8=subjudul8)


@app.route('/videopembelajaran')
def videopembelajaran():
    judul = "Video Pembelajaran"
    subjudul1 = "Wujud Benda"
    subjudul2 = "Perubahan Wujud Benda"
    return render_template('videopembelajaran.html', judul=judul, subjudul1=subjudul1, subjudul2=subjudul2,)


@app.route('/quiz')
def quiz():
    judul = "Quiz"
    subjudul1 = "Mari kerjakan quiz!"
    return render_template('quiz.html', judul=judul, subjudul1=subjudul1,)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
