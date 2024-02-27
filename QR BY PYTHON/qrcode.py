import segno

link = input("Enter the link: ")
qrc = segno.make_qr(link)
qrc.save(".qrcode.png",
          scale = 5,
            light = "gainsboro",
            dark = "midnightblue",
            quiet_zone = "lightgray",
            data_dark = "black"
            )
