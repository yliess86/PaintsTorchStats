let UUID  = null;
let FILES = [];
let FILE  = null;
let N     = 0;
let I     = 0;

let reset_session = function() {
    UUID  = null;
    FILES = [];
    FILE  = null;
    N     = 0;
    I     = 0;
};

let shuffle = function(array) {
    array.sort(() => Math.random() - 0.5);
}; 

let gen_uuid = function() {
    UUID = ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(
        /[018]/g,
        c => (c ^ crypto.getRandomValues(
            new Uint8Array(1))[0] & 15 >> c / 4
        ).toString(16)
    );
};

let get_next = function() {
    if(FILES.length <= 0) {
        $('#rating').addClass('hidden');
        $('#new').removeClass('hidden');
        return;
    }

    FILE = FILES.pop();
    I   += 1;
    
    $('#progressbar-inner').css('width', (I / N * 100) + '%');

    $.ajax({
        url     : 'https://dvic.devinci.fr/dgx/paints_torch/api/v1/study/' + FILE,
        type    : 'GET',
        success : function(response){
            $('#illustration').attr('src', response.illustration);
            $('#submit').removeClass('hidden');
        }
    });
};

let get_list = () => {
    $.ajax({
        url     : 'https://dvic.devinci.fr/dgx/paints_torch/api/v1/study',
        type    : 'GET',
        success : function(response){
            FILES = response.files;
            N     = FILES.length;
            shuffle(FILES);
            get_next();
        }
    });
};

let new_session = function() {
    reset_session();

    gen_uuid();
    get_list();
    
    $('#new').addClass('hidden');
    $('#rating').removeClass('hidden');
};

let submit = function() {
    $('#rate input[name="rate"]').attr('checked', false);
    $('#fair').attr('checked', true);
    $('#submit').addClass('hidden');
    
    let rate = parseInt($('#rate input[name="rate"]:checked').val()); 
    let data = {
        uuid      : UUID,
        file_name : FILE,
        rate      : rate
    };
    
    $.ajax({
        url         : 'https://dvic.devinci.fr/dgx/paints_torch/api/v1/study',
        type        : 'POST',
        data        : JSON.stringify(data),
        contentType : 'application/json; charset=utf-8',
        dataType    : 'json'
    });
    
    get_next();
}