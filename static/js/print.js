function printQR() {
    var qrImage = document.getElementById("qrCodeImage");
    
    if (qrImage) {
        qrImage = qrImage.src;
        var printWindow = window.open('', '_blank');
        printWindow.document.write('<img src="' + qrImage + '">');
        printWindow.document.close();
        printWindow.print();
        printWindow.close();
    } else {
        console.error("QR code image element not found.");
    }
}