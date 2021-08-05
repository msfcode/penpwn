# accespwn 🐱‍👤 V2.0
 
   I built this tool to make pentesting easier and I will try to always add new options:
   Accespwn project is coded by msfcode (instagram.com/msfcode) , the 12/11/2020, you can use
   this awsome tool for mac changing, arp spoofing, sniffing, subfinding, get websites ip, get mac address ip's, BOOM MAILING, 
   Generate Ngrok link, localhost.run link (ssh) also you can generates Backdoors and keyloggers and PHISHING pages like Paypal and snapchat
   At this moment im working at Login Page BruteForcing and Web App vulnerability scanner

 




i will work at Exploits, i will add some exploits that is coded by me, also i will make an smart Fuzzer to generate exploit...
## About 
    Author : msfcode
    Instagram : instagram.com/msfcode
    Github : github.com/msfcode
    Principal Prog Lang : python3 
    Others : html, css, js
    Project : accespwn
    version : 2.0
# Donation 💲
If you want to help us , to keep going and try to add new options and attacks or exploits :
<p><a href="https://www.buymeacoffee.com/msfcode"> <img align="left" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="50" width="210" alt="msfcode" /></a></p><br><br>   

<div id="smart-button-container">
      <div style="text-align: center;">
        <div id="paypal-button-container"></div>
      </div>
    </div>
  <script src="https://www.paypal.com/sdk/js?client-id=sb&enable-funding=venmo&currency=USD" data-sdk-integration-source="button-factory"></script>
  <script>
    function initPayPalButton() {
      paypal.Buttons({
        style: {
          shape: 'pill',
          color: 'gold',
          layout: 'horizontal',
          label: 'pay',
          
        },

        createOrder: function(data, actions) {
          return actions.order.create({
            purchase_units: [{"description":"Support me with just 1$ . Thank Yoy","amount":{"currency_code":"USD","value":1}}]
          });
        },

        onApprove: function(data, actions) {
          return actions.order.capture().then(function(orderData) {
            
            // Full available details
            console.log('Capture result', orderData, JSON.stringify(orderData, null, 2));

            // Show a success message within this page, e.g.
            const element = document.getElementById('paypal-button-container');
            element.innerHTML = '';
            element.innerHTML = '<h3>Thank you for your payment!</h3>';

            // Or go to another URL:  actions.redirect('thank_you.html');
            
          });
        },

        onError: function(err) {
          console.log(err);
        }
      }).render('#paypal-button-container');
    }
    initPayPalButton();
  </script>
   
   # Installation 🔶
   NB : Be root before using it (sudo su)
   ##    step 1 (launch setup file)
    root@kali:~# python3 setup.py
        NB : if you get any errors contact msfcode at instagram.com
        
   ##    step 2 (execute accespwn tool)
    root@kali:~# pyhon3 accespwn.py --help
     NB : type y after enter this command if you want to use the Command line interface
    Or 
    root@kali:~# python3 accespwn.py
   
       
