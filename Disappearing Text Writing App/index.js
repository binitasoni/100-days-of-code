var timer = null;
    $('#name').keyup(function(){
           clearTimeout(timer); 
           timer = setTimeout(doStuff, 1000)
    });
    
    function doStuff() {
        document.getElementById('name').value = '';
    }
