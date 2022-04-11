document.addEventListener('DOMContentLoaded', function(){
    let alertGreen = document.querySelector('#alert_green');
    let alertRed = document.querySelector('#alert_red');

    alertGreen.style.display = "none";
    alertRed.style.display = "none";

    form = document.querySelector('#form')

    form.addEventListener('submit', handleSubmit);
});


handleSubmit = (event) => {

    event.preventDefault();

    let name = document.querySelector('#name').value;
    let email = document.querySelector('#email').value;
    let subject = document.querySelector('#subject').value;
    let message = document.querySelector('#message').value; 
    let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    
   

    const request = new Request(
        'http://localhost:8000',
        {headers: {'X-CSRFToken': csrftoken}}
    )

    fetch(request ,{
        method: 'POST',
        mode: 'same-origin',
        body: JSON.stringify({
            name: name,
            email: email,
            subject: subject,
            message: message
        })
    })
    .then(response => response.json())
    .then(res => {
        if (res.ok){
            document.querySelector("form").reset();
            document.querySelector("#message").innerHTML = 'How can I help?'

            let alertGreen = document.querySelector('#alert_green');
    
            alertGreen.style.display = "block";
        
            setTimeout(function(){
                alertGreen.style.display = "none";
            },5000);
        }
        else{
            let alertRed = document.querySelector('#alert_red');
           

            
            alertRed.style.display = "block";
            
            
            setTimeout(function(){
                alertRed.style.display = "none";
            },5000);
        }
    }
    )};

clean = () =>{
    document.querySelector("#message").innerHTML = "";
}