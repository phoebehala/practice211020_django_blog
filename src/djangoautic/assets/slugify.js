const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

// value will be the title a user enter
// .trim() >>> trim white space
const slugify = (value)=>{
    return value.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')         // Replace & with 'and'
        .replace(/[\s\W-]+/g, '-')      // Replace spaces, non-word characters and dashes with a single dash (-)
}

titleInput.addEventListener('keyup', (event)=>{
    slugInput.setAttribute('value', slugify(titleInput.value));
})
