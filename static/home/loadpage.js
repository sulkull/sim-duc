$(document).ready(function() {
        size_li = $(".photo-grid.clearfix ul.clearfix.sim-moi li#sim-moi").size();  //chon phan tu - item
        x = 36; // so luong item hien thi
        hiddenBtn = document.querySelector('#showLess');
        hiddenBtn.style.display = 'none';
        $('.photo-grid.clearfix ul.clearfix.sim-moi li#sim-moi:lt(' + x + ')').show();
        $('#loadMore').click(function() {
            x = (x + 9 <= size_li) ? x + 9 : size_li;  // so item 1 lan load
            $('.photo-grid.clearfix ul.clearfix.sim-moi li#sim-moi:lt(' + x + ')').show();
            hiddenBtn.style.display = 'block';
        });
        $('#showLess').click(function() {
            x = (x - 9 < 0) ? 9 : x - 9; // so item 1 lan hidden
            $('.photo-grid.clearfix ul.clearfix.sim-moi li#sim-moi').not(':lt(' + x + ')').hide();
            if (x <= 9) {  // neu so item < 9 thi hidden button showless
                hiddenBtn.style.display = 'none';
            } else {
                hiddenBtn.style.display = 'block';
            }
        });
    });