const body = document.getElementsByTagName('body')[0];
const all = document.getElementsByTagName("*");
const mySelect = document.getElementById('source-selector');
let sourceName = document.getElementById('source-for-selector').defaultValue;
const newButton = document.getElementById('new-button');

let beginSliceInd = sourceName.indexOf('/');
let endSliceIndex = sourceName.indexOf('.');
sourceName  = sourceName.slice(beginSliceInd+1, endSliceIndex);

// sets correct value to dropdown menu and applys specific styles
for(let i, j = 0; i = mySelect.options[j]; j++) {
    if(i.value == sourceName) {
        mySelect.selectedIndex = j;
        for(let k=0; k<all.length; k++){
            body.classList.add(sourceName)
        }
        break;
    }
}

// gets the conversion table for titles so that they are "readable"
let conversionObj = {}
for(let i=0; i<mySelect.options.length; i++){
    conversionObj = Object.assign(conversionObj, {[mySelect.options[i].value]: mySelect.options[i].text})
    localStorage[mySelect.options[i].value] =  mySelect.options[i].text
}

// STUFF TO MAKE SENTENCE LOOK LIKE ITS TYPED
let sentence = document.getElementById('sentence-to-show').innerText

function loadScript (dir, file) {
    var scr = document.createElement("script")
    scr.src = dir + file
    document.body.appendChild(scr)
}

let options = {
    strings: [sentence],
    typeSpeed: 15,
    backDelay: 700,
    backSpeed: 20,
    cursorChar: "",
};

let typed = new Typed("#typed", options);

function resetTyped(newTexts) {
    const dataType = newTexts;
    if (dataType === undefined) {
      return false;
    }
    const strings = ['', dataType];
    if(typed && typed.constructor === Typed) {
      typed.destroy();
    }
    typed = new Typed('#typed', {
        strings: strings,
        typeSpeed: 15,
        backDelay: 700,
        backSpeed: 20,
        cursorChar: "",
    });
};

// Vanilla
function AJAX_new_sentence(callback) {
    let oColor = newButton.style.backgroundColor
    // edit css
    newButton.style.backgroundColor='#f00'
    const httpRequest = new XMLHttpRequest()
    httpRequest.open('POST', `/sentence/${sourceName}`, true)
    httpRequest.send()
    httpRequest.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200) {
            sentence = this.responseText
            resetTyped(sentence)
            // revert css
            // callback
            newButton.style.backgroundColor=oColor
        }
    }
}

function changeCSS() {
    newButton.classList.add('loading')
}
