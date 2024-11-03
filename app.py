from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Data dummy untuk toko ATK
produk_data = {
    "1": {"name": "Pulpen", "category": "Alat Tulis", "price": 2000, "stock": 100},
    "2": {"name": "Pensil", "category": "Alat Tulis", "price": 1500, "stock": 200},
    "3": {"name": "Penghapus", "category": "Alat Tulis", "price": 1000, "stock": 300},
    "4": {"name": "Penggaris", "category": "Alat Ukur", "price": 5000, "stock": 50},
    "5": {"name": "Buku Tulis", "category": "Kertas", "price": 8000, "stock": 150},
    "6": {"name": "Stapler", "category": "Organizer", "price": 15000, "stock": 30},
    "7": {"name": "Clip Kertas", "category": "Organizer", "price": 500, "stock": 500},
    "8": {"name": "Correction Tape", "category": "Alat Tulis", "price": 8000, "stock": 200},
    "9": {"name": "Map", "category": "Organizer", "price": 2000, "stock": 100},
    "10": {"name": "Spidol", "category": "Alat Tulis", "price": 6000, "stock": 80},
    "11": {"name": "Sticky Note", "category": "Kertas", "price": 2500, "stock": 75},
    "12": {"name": "Highlighter", "category": "Alat Tulis", "price": 8000, "stock": 40},
    "13": {"name": "Binder", "category": "Kertas", "price": 12000, "stock": 25},
    "14": {"name": "Box File", "category": "Organizer", "price": 15000, "stock": 450},
    "15": {"name": "Watercolor Paper", "category": "Peralatan Gambar", "price": 20000, "stock": 15},
}

kategori_data = {
    "1": {"name": "Alat Tulis"},
    "2": {"name": "Kertas"},
    "3": {"name": "Perlengkapan Kantor"},
    "4": {"name": "Peralatan Gambar"},
    "5": {"name": "Perlengkapan Sekolah"},
    "6": {"name": "Produk Perekat"},
    "7": {"name": "Organizer"},
    "8": {"name": "Peralatan Komputer"},
    "9": {"name": "Perlengkapan Meja"},
    "10": {"name": "Perlengkapan Elektronik"},
    "11": {"name": "Alat Ukur"},
    "12": {"name": "Produk Dekorasi"},
    "13": {"name": "Alat Hitung"},
    "14": {"name": "Buku Catatan Khusus"},
    "15": {"name": "Amplop dan Perangko"},
}

pelanggan_data = {
    "1": {"name": "Lois", "email": "lois@gmail.com"},
    "2": {"name": "Firman", "email": "firman@gmail.com"},
    "3": {"name": "Naya", "email": "naya@gmail.com"},
    "4": {"name": "Ifa", "email": "Ifa@gmail.com"},
    "5": {"name": "Bayu", "email": "bayu@gmail.com"},
    "6": {"name": "Faisal", "email": "faisal@gmail.com"},
    "7": {"name": "Gina", "email": "gina@gmail.com"},
    "8": {"name": "Haris", "email": "haris@gmail.com"},
    "9": {"name": "Nisa", "email": "nisa@gmail.com"},
    "10": {"name": "Naufal", "email": "naufal@gmail.com"},
    "11": {"name": "Raian", "email": "raian@gmail.com"},
    "12": {"name": "Gishela", "email": "gishela@gmail.com"},
    "13": {"name": "Tasya", "email": "tasya@gmail.com"},
    "14": {"name": "Ganin", "email": "ganin@gmail.com"},
    "15": {"name": "Ruben", "email": "ruben@gmail.com"},
}

# Endpoint untuk Produk
class ProdukList(Resource):
    def get(self):
        return jsonify(produk_data)

    def post(self):
        new_id = str(len(produk_data) + 1)
        data = request.json
        produk_data[new_id] = data
        return jsonify(produk_data[new_id]), 201

class Produk(Resource):
    def get(self, produk_id):
        produk = produk_data.get(produk_id)
        return jsonify(produk) if produk else ('Produk tidak ditemukan', 404)

    def put(self, produk_id):
        if produk_id in produk_data:
            data = request.json
            produk_data[produk_id].update(data)
            return jsonify(produk_data[produk_id])
        return ('Produk tidak ditemukan', 404)

    def delete(self, produk_id):
        if produk_id in produk_data:
            deleted_produk = produk_data.pop(produk_id)
            return jsonify(deleted_produk)
        return ('Produk tidak ditemukan', 404)

# Endpoint untuk Kategori
class KategoriList(Resource):
    def get(self):
        return jsonify(kategori_data)

    def post(self):
        new_id = str(len(kategori_data) + 1)
        data = request.json
        kategori_data[new_id] = data
        return jsonify(kategori_data[new_id]), 201

class Kategori(Resource):
    def get(self, kategori_id):
        kategori = kategori_data.get(kategori_id)
        return jsonify(kategori) if kategori else ('Kategori tidak ditemukan', 404)

    def put(self, kategori_id):
        if kategori_id in kategori_data:
            data = request.json
            kategori_data[kategori_id].update(data)
            return jsonify(kategori_data[kategori_id])
        return ('Kategori tidak ditemukan', 404)

    def delete(self, kategori_id):
        if kategori_id in kategori_data:
            deleted_kategori = kategori_data.pop(kategori_id)
            return jsonify(deleted_kategori)
        return ('Kategori tidak ditemukan', 404)

# Endpoint untuk Pelanggan
class PelangganList(Resource):
    def get(self):
        return jsonify(pelanggan_data)

    def post(self):
        new_id = str(len(pelanggan_data) + 1)
        data = request.json
        pelanggan_data[new_id] = data
        return jsonify(pelanggan_data[new_id]), 201

class Pelanggan(Resource):
    def get(self, pelanggan_id):
        pelanggan = pelanggan_data.get(pelanggan_id)
        return jsonify(pelanggan) if pelanggan else ('Pelanggan tidak ditemukan', 404)

    def put(self, pelanggan_id):
        if pelanggan_id in pelanggan_data:
            data = request.json
            pelanggan_data[pelanggan_id].update(data)
            return jsonify(pelanggan_data[pelanggan_id])
        return ('Pelanggan tidak ditemukan', 404)

    def delete(self, pelanggan_id):
        if pelanggan_id in pelanggan_data:
            deleted_pelanggan = pelanggan_data.pop(pelanggan_id)
            return jsonify(deleted_pelanggan)
        return ('Pelanggan tidak ditemukan', 404)

# Menambahkan resource ke API
api.add_resource(ProdukList, '/produk')
api.add_resource(Produk, '/produk/<produk_id>')
api.add_resource(KategoriList, '/kategori')
api.add_resource(Kategori, '/kategori/<kategori_id>')
api.add_resource(PelangganList, '/pelanggan')
api.add_resource(Pelanggan, '/pelanggan/<pelanggan_id>')

if __name__ == '__main__':
    app.run(debug=True)
