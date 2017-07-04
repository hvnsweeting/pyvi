import unittest

import pytho.poetry


class Test7Words4Sentences(unittest.TestCase):
    def test_ltvb(self):
        poem = '''Thuở ấy tuy còn tuổi ấu thơ
        Mà sao vẫn nhớ đến bây giờ
        Xuân về nũng nịu đòi mua pháo
        Để đón giao thừa thỏa ước mơ'''.split('\n')

        self.assertTrue(pytho.poetry.validate_ltvb(poem))

    def test_hai_sac_hoa_tigon_ltvb(self):
        hshtg = '''Nếu biết rằng tôi đã lấy chồng,
        Trời ơi! Người ấy có buồn không?
        Có thầm nghĩ tới loài hoa... vỡ
        Tựa trái tim phai, tựa máu hồng?'''
        self.assertFalse(pytho.poetry.validate_ltvb(hshtg))

    def test_lbvb(self):
        poem = '''Rừng phong nhuộm tím cả khung trời
        Lá úa lìa cành gió cuốn rơi
        Lối cũ đường xưa em đếm bước
        Miên man kỷ niệm đã xa vời'''

        self.assertTrue(pytho.poetry.validate_lbvb(poem))

    def test_not_ltvb(self):
        tau_lo = '''Tẩu Lộ tài tri tẩu lộ nan
        Trùng san chi ngoại hựu trùng san
        Trùng san đăng đáo cao phong hậu
        Vạn lý dư đồ cố miện gian'''.split('\n')
        self.assertFalse(pytho.poetry.validate_ltvb(tau_lo))

    def test_ltvb_2v(self):
        poem = '''Xác pháo còn vương màu mực tím
        Thư tình vẫn thắm chữ yêu thương
        Nhưng ai lại nỡ quên thề ước
        Nước mắt nào vơi nỗi đoạn trường '''
        self.assertTrue(pytho.poetry.validate_ltvb_2v(poem))

    def test_lbvb_2v(self):
        poem = '''Hè về đỏ thắm màu hoa phượng
        Ánh mắt buồn tênh buổi bãi trường
        Gạt lệ chia tay người mỗi ngã
        Âm thầm cố nén giọt sầu thương'''
        self.assertTrue(pytho.poetry.validate_lbvb_2v(poem))


if __name__ == "__main__":
    unittest.main()
