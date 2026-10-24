import time

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class MoverNode(Node):

    def __init__(self):
        super().__init__('controller')

        # =========================================
        # PUBLISHER /cmd_vel
        # =========================================
        self.cmd_pub = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        # =========================================
        # PARAMETER FISIK ROBOT
        # =========================================
        self.wheel_radius = 0.030
        self.wheel_separation = 0.170

        # =========================================
        # KONFIGURASI LINTASAN MANUAL
        #
        # mode:
        #   'wheel' = gunakan L_speed dan R_speed
        #   'cmd'   = gunakan linear dan angular
        #
        # L_speed : kecepatan roda kiri (rad/s)
        # R_speed : kecepatan roda kanan (rad/s)
        # linear  : kecepatan maju/mundur (m/s)
        # angular : kecepatan putar (rad/s)
        # durasi  : lama gerakan (detik)
        # =========================================
        self.lintasan = [

            # -------------------------------------
            # TAHAP 1: SETUP
            # -------------------------------------
            {
                'tahap': 1,
                'mode': 'wheel',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 0.0,
                'angular': 0.0,
                'durasi': 5.0,
            },

            # -------------------------------------
            # TAHAP 2: PUTAR KIRI
            # -------------------------------------
            {
                'tahap': 2,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 0.0,
                'angular': 1.0,
                'durasi': 2.555,
            },

            # -------------------------------------
            # TAHAP 3: MAJU 1
            # -------------------------------------
            {
                'tahap': 3,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 1.0,
                'angular': 0.0,
                'durasi': 10.2,
            },

            # -------------------------------------
            # TAHAP 4: PUTAR KANAN
            # -------------------------------------
            {
                'tahap': 4,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 0.0,
                'angular': -1.0,
                'durasi': 2.555,
            },

            # -------------------------------------
            # TAHAP 5: MAJU 2
            # -------------------------------------
            {
                'tahap': 5,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 1.0,
                'angular': 0.0,
                'durasi': 10.2,
            },

            # -------------------------------------
            # TAHAP 6: KIRI
            # -------------------------------------
            {
                'tahap': 6,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 0.0,
                'angular': 1.0,
                'durasi': 2.56,
            },

            # -------------------------------------
            # TAHAP 7: Maju 3
            # -------------------------------------
            {
                'tahap': 7,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 1.0,
                'angular': 0.0,
                'durasi': 2.7,
            },

            # -------------------------------------
            # TAHAP 8: Kanan
            # -------------------------------------
            {
                'tahap': 8,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 0.0,
                'angular': -1.0,
                'durasi': 2.555,
            },

            # -------------------------------------
            # TAHAP 9: Maju 4
            # -------------------------------------
            {
                'tahap': 9,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 1.0,
                'angular': 0.0,
                'durasi': 5.2,
            },

            # -------------------------------------
            # TAHAP 10: Kanan
            # -------------------------------------
            {
                'tahap': 10,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 0.0,
                'angular': -1.0,
                'durasi': 2.56,
            },

            # -------------------------------------
            # TAHAP 11: Maju 5
            # -------------------------------------
            {
                'tahap': 11,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 1.0,
                'angular': 0.0,
                'durasi': 9.7,
            },

            # -------------------------------------
            # TAHAP 12 : Kiri
            # -------------------------------------
            {
                'tahap': 12,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 0.0,
                'angular': 1.0,
                'durasi': 2.56,
            },
            # -------------------------------------
            # TAHAP 13: Maju
            # -------------------------------------
            {
                'tahap': 13,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 1.0,
                'angular': 0.0,
                'durasi': 18.2,
            },

            # -------------------------------------
            # TAHAP 14 : Kiri
            # -------------------------------------
            {
                'tahap': 14,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 0.0,
                'angular': 1.0,
                'durasi': 2.56,
            },
            # -------------------------------------
            # TAHAP 15: Maju
            # -------------------------------------
            {
                'tahap': 15,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 1.0,
                'angular': 0.0,
                'durasi': 21.2,
            },
            # -------------------------------------
            # TAHAP 16: Lengkung
            # -------------------------------------
            {
                'tahap': 16,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 1.0,
                'angular': 0.25,
                'durasi': 20.0,
            },

            # -------------------------------------
            # TAHAP 17 : Kanan
            # -------------------------------------
            {
                'tahap': 17,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 0.0,
                'angular': 1.0,
                'durasi': 0.2,
            },
            # -------------------------------------
            # TAHAP 18: Maju
            # -------------------------------------
            {
                'tahap': 18,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 1.0,
                'angular': 0.0,
                'durasi': 7.0,
            },

            # -------------------------------------
            # TAHAP 19 : Kanan
            # -------------------------------------
            {
                'tahap': 19,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 0.0,
                'angular': -1.0,
                'durasi': 2.555,
            },
            # -------------------------------------
            # TAHAP 20: Maju
            # -------------------------------------
            {
                'tahap': 20,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 1.0,
                'angular': 0.0,
                'durasi': 4.1,
            },

            # -------------------------------------
            # TAHAP 21 : Kanan
            # -------------------------------------
            {
                'tahap': 21,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 0.0,
                'angular': -1.0,
                'durasi': 2.57,
            },
            # -------------------------------------
            # TAHAP 22: Maju
            # -------------------------------------
            {
                'tahap': 22,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 1.0,
                'angular': 0.0,
                'durasi': 10.5,
            },

            # -------------------------------------
            # TAHAP 23 : Kiri
            # -------------------------------------
            {
                'tahap': 23,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 0.0,
                'angular': 1.0,
                'durasi': 2.555,
            },
            # -------------------------------------
            # TAHAP 24: Maju
            # -------------------------------------
            {
                'tahap': 24,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 1.0,
                'angular': 0.0,
                'durasi': 9.5,
            },

            # -------------------------------------
            # TAHAP 25 : Kanan
            # -------------------------------------
            {
                'tahap': 25,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 0.0,
                'angular': -1.0,
                'durasi': 2.56,
            },
            # -------------------------------------
            # TAHAP 26: Maju
            # -------------------------------------
            {
                'tahap': 26,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 1.0,
                'angular': 0.0,
                'durasi': 3.5,
            },

            # -------------------------------------
            # TAHAP 27 : Kiri
            # -------------------------------------
            {
                'tahap': 27,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 0.0,
                'angular': 1.0,
                'durasi': 2.56,
            },
            # -------------------------------------
            # TAHAP 28: Maju
            # -------------------------------------
            {
                'tahap': 28,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 1.0,
                'angular': 0.0,
                'durasi': 6.0,
            },
            # -------------------------------------
            # TAHAP 29 : Kiri
            # -------------------------------------
            {
                'tahap': 29,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 0.0,
                'angular': 1.0,
                'durasi': 2.55,
            },
            # -------------------------------------
            # TAHAP 30: Maju
            # -------------------------------------
            {
                'tahap': 30,
                'mode': 'cmd',
                'L_speed': 0.0,
                'R_speed': 0.0,
                'linear': 1.0,
                'angular': 0.0,
                'durasi': 9.0,
            },
        ]

        # =========================================
        # STATUS PROGRAM
        # =========================================
        self.indeks = 0
        self.waktu_mulai = None
        self.waktu_tahap = None
        self.selesai = False
        self.tahap_dimulai = False

        # Timer kontrol 20 Hz
        self.timer = self.create_timer(
            0.05,
            self.kontrol
        )

        # =========================================
        # INFORMASI PROGRAM
        # =========================================
        self.get_logger().info(
            '========================================'
        )
        self.get_logger().info(
            '       MOVER NODE - MAZE MOVER'
        )
        self.get_logger().info(
            '========================================'
        )
        self.get_logger().info(
            'Topic: /cmd_vel'
        )
        self.get_logger().info(
            'Mode kontrol: konfigurasi manual'
        )
        self.get_logger().info(
            f'Wheel radius: {self.wheel_radius:.3f} m'
        )
        self.get_logger().info(
            f'Wheel separation: {self.wheel_separation:.3f} m'
        )
        self.get_logger().info(
            f'Jumlah tahap: {len(self.lintasan)}'
        )
        self.get_logger().warning(
            'Kontrol open-loop: tidak menggunakan odometri.'
        )

    # =============================================
    # KIRIM PERINTAH KE /cmd_vel
    # =============================================
    def kirim_cmd(self, linear, angular):

        msg = Twist()

        msg.linear.x = float(linear)
        msg.angular.z = float(angular)

        self.cmd_pub.publish(msg)

    # =============================================
    # FORWARD KINEMATICS
    # Kecepatan roda -> linear dan angular
    # =============================================
    def forward_kinematics(
        self,
        left_speed,
        right_speed
    ):

        r = self.wheel_radius
        L = self.wheel_separation

        linear = r * (
            right_speed + left_speed
        ) / 2.0

        angular = r * (
            right_speed - left_speed
        ) / L

        return linear, angular

    # =============================================
    # INVERSE KINEMATICS
    # Linear dan angular -> kecepatan roda
    # =============================================
    def inverse_kinematics(
        self,
        linear,
        angular
    ):

        r = self.wheel_radius
        L = self.wheel_separation

        left_speed = (
            linear - angular * L / 2.0
        ) / r

        right_speed = (
            linear + angular * L / 2.0
        ) / r

        return left_speed, right_speed

    # =============================================
    # KONTROL LINTASAN
    # =============================================
    def kontrol(self):

        # Jika program sudah selesai, pertahankan stop
        if self.selesai:
            self.kirim_cmd(0.0, 0.0)
            return

        sekarang = time.monotonic()

        # =========================================
        # MULAI STOPWATCH
        # =========================================
        if self.waktu_mulai is None:

            self.waktu_mulai = sekarang
            self.waktu_tahap = sekarang

            self.get_logger().info(
                'START: lintasan otomatis dimulai.'
            )

        # =========================================
        # CEK AKHIR LINTASAN
        # =========================================
        if self.indeks >= len(self.lintasan):

            self.kirim_cmd(0.0, 0.0)

            durasi_total = (
                sekarang - self.waktu_mulai
            )

            self.selesai = True

            self.get_logger().info(
                '========================================'
            )
            self.get_logger().info(
                'LINTASAN SELESAI'
            )
            self.get_logger().info(
                f'Durasi total: {durasi_total:.2f} detik'
            )
            self.get_logger().info(
                'Robot diperintahkan berhenti.'
            )
            self.get_logger().info(
                '========================================'
            )

            return

        # =========================================
        # AMBIL KONFIGURASI TAHAP AKTIF
        # =========================================
        tahap = self.lintasan[self.indeks]

        nomor = tahap['tahap']
        mode = tahap['mode']
        durasi = tahap['durasi']

        # =========================================
        # MODE WHEEL
        # Gunakan L_speed dan R_speed
        # =========================================
        if mode == 'wheel':

            left_speed = tahap['L_speed']
            right_speed = tahap['R_speed']

            linear, angular = self.forward_kinematics(
                left_speed,
                right_speed
            )

        # =========================================
        # MODE CMD
        # Gunakan linear dan angular
        # =========================================
        elif mode == 'cmd':

            linear = tahap['linear']
            angular = tahap['angular']

            # Hitung kecepatan roda untuk monitoring
            left_speed, right_speed = (
                self.inverse_kinematics(
                    linear,
                    angular
                )
            )

        else:

            self.get_logger().error(
                f'Mode tidak valid pada tahap {nomor}.'
            )

            self.kirim_cmd(0.0, 0.0)
            self.selesai = True

            return

        # =========================================
        # TAMPILKAN INFORMASI TAHAP SATU KALI
        # =========================================
        if not self.tahap_dimulai:

            self.get_logger().info(
                '----------------------------------------'
            )
            self.get_logger().info(
                f'Memulai tahap {nomor}'
            )
            self.get_logger().info(
                f'Mode: {mode}'
            )
            self.get_logger().info(
                f'L speed: {left_speed:.3f} rad/s'
            )
            self.get_logger().info(
                f'R speed: {right_speed:.3f} rad/s'
            )
            self.get_logger().info(
                f'Linear: {linear:.3f} m/s'
            )
            self.get_logger().info(
                f'Angular: {angular:.3f} rad/s'
            )
            self.get_logger().info(
                f'Durasi: {durasi:.2f} detik'
            )

            self.tahap_dimulai = True

        # =========================================
        # JALANKAN GERAKAN
        # =========================================
        self.kirim_cmd(
            linear,
            angular
        )

        # =========================================
        # CEK DURASI
        # =========================================
        if sekarang - self.waktu_tahap >= durasi:

            # Berhenti sebelum tahap selanjutnya
            self.kirim_cmd(0.0, 0.0)

            self.get_logger().info(
                f'Tahap {nomor} selesai.'
            )

            self.indeks += 1
            self.waktu_tahap = sekarang
            self.tahap_dimulai = False

    # =============================================
    # MATIKAN NODE
    # =============================================
    def destroy_node(self):

        try:
            self.kirim_cmd(0.0, 0.0)
        except Exception:
            pass

        super().destroy_node()


# =============================================
# FUNGSI UTAMA
# =============================================
def main(args=None):

    rclpy.init(args=args)

    node = MoverNode()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        node.get_logger().info(
            'Program dihentikan oleh pengguna.'
        )

    finally:

        try:
            node.kirim_cmd(0.0, 0.0)
        except Exception:
            pass

        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
