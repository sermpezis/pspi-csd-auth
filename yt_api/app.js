const KEY = 'put_here_your_API_key';
let query = "";
const numResults = 3;

const input = document.querySelector('input');
const form = document.querySelector('form');

updateInput = (e) => {
    query = e.target.value;
}
input.addEventListener('input', updateInput);

submitted = (event) => {
    event.preventDefault();
    getImages();
}

form.onsubmit = submitted.bind(form);

getImages = () => {
    fetch(`https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=${numResults}&q=${query}&key=${KEY}`)
    .then(res => res.json())
    .then(data => {
        const innerImages = document.querySelectorAll('.image');
        const innerTexts = document.querySelectorAll('.text');
        const imageList = data.items;
        for (i=0;i<innerImages.length;i++) {
            innerImages[i].innerHTML = `<img class="img-fluid" src="${imageList[i].snippet.thumbnails.medium.url}" />`;
            // innerImages[i].innerHTML = `<img class="img-fluid" src="${imageList[i].snippet.thumbnails.medium.url}" /> <span>${imageList[i].snippet.title}</span>`;
        }
    })
}
