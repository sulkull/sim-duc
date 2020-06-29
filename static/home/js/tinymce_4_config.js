// TinyMCE 4 configuration
// Modify the following code to customize TinyMCE

tinymce.init({
	selector: "textarea#id_NoiDung",
	plugins: 'print preview fullpage powerpaste searchreplace autolink directionality advcode visualblocks visualchars fullscreen image link media mediaembed template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists wordcount tinymcespellchecker a11ychecker imagetools textpattern help formatpainter permanentpen pageembed tinycomments mentions linkchecker',
    toolbar1: "bold italic underline strikethrough | blockquote | bullist numlist | subscript superscript | table | hr | formatselect fontselect fontsizeselect addcomment",
	toolbar2: "undo redo | forecolor backcolor | link unlink | image media | alignleft aligncenter alignright alignjustify | outdent indent | charmap emoticons | searchreplace | removeformat code | preview fullscreen",

	// Aditional options. Customize them as per your needs.
	height: 350,
	resize: "both",
	image_advtab: true,
	importcss_append: true,
    spellchecker_dialog: true,
	toolbar_items_size: "medium",
	menubar: true,
	//file_picker_types: 'image',
    file_picker_callback: function (cb, value, meta) {
    var input = document.createElement('input');
    input.setAttribute('type', 'file');
    input.setAttribute('accept', 'image/*');
    input.onchange = function () {
        var file = this.files[0];
        var reader = new FileReader();
        reader.onload = function () {
            var id = 'blobid' + (new Date()).getTime();
            var blobCache =  tinymce.activeEditor.editorUpload.blobCache;
            var base64 = reader.result.split(',')[1];
            var blobInfo = blobCache.create(id, file, base64);
            blobCache.add(blobInfo);
            cb(blobInfo.blobUri(), { title: file.name });
        };
      reader.readAsDataURL(file);
    };

    input.click();
    },
    content_css : "/static/home/css/style.css",
});