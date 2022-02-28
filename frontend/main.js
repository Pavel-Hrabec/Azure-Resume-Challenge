window.addEventListener('DOMContentLoaded', (event) =>{ // Everytime content is loaded go and run the getVisitCount 
    getVisitCount();
})

const functionApiUrl = '';
// const localFunctionApi = 'http://localhost:7071/api/GetResumeCounter';

const getVisitCount = () => {
    let count = 30;
    fetch(functionApiUrl).then(response => { // fetch will get data supplied by API fuction, once you do that, grab the response and 
        return response.json() // return it json
    }).then(response =>{ // grab the response in json 
        console.log("Website called function API."); //log for debugging, just in case
        count =  response.count; // we will count value in rensponse
        document.getElementById("counter").innerText = count; // Go into the document, find the element that has counter as it's id and set the value to count 
    }).catch(function(error){ // if there is an error we will grab it and 
        console.log(error); // display it in console
    });
    return count; // 
}