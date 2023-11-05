$(document).on('submit', '#post-form', function(e){
    e.preventDefault();
    $.ajax({
        type:'POST',
        url:'{% url "mental:Questionnaire"%}',
        data:{
            Q1A:$('#Q1A').val(),
            Q2A:$('#Q2A').val(),
            Q3A:$('#Q3A').val(),
            Q4A:$('#Q4A').val(),
            Q5A:$('#Q5A').val(),
            Q6A:$('#Q6A').val(),
            Q7A:$('#Q7A').val(),
            Q8A:$('#Q8A').val(),
            Q9A:$('#Q9A').val(),
            Q10A:$('#Q10A').val(),
            Q11A:$('#Q11A').val(),
            Q12A:$('#Q12A').val(),
            Q13A:$('#Q13A').val(),
            Q14A:$('#Q14A').val(),
            Q15A:$('#Q15A').val(),
            Q16A:$('#Q16A').val(),
            Q17A:$('#Q17A').val(),
            Q18A:$('#Q18A').val(),
            Q19A:$('#Q19A').val(),
            Q20A:$('#Q20A').val(),
            Q21A:$('#Q21A').val(),
            Q22A:$('#Q22A').val(),
            Q23A:$('#Q23A').val(),
            Q24A:$('#Q24A').val(),
            Q25A:$('#Q25A').val(),
            Q26A:$('#Q26A').val(),
            Q27A:$('#Q27A').val(),
            Q28A:$('#Q28A').val(),
            Q29A:$('#Q29A').val(),
            Q30A:$('#Q30A').val(),
            Q31A:$('#Q31A').val(),
            Q32A:$('#Q32A').val(),
            Q33A:$('#Q33A').val(),
            Q34A:$('#Q34A').val(),
            Q35A:$('#Q35A').val(),
            Q36A:$('#Q36A').val(),
            Q37A:$('#Q37A').val(),
            Q38A:$('#Q38A').val(),
            Q39A:$('#Q39A').val(),
            Q40A:$('#Q40A').val(),
            Q41A:$('#Q41A').val(),
            Q42A:$('#Q42A').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            action:'post'
        },
        
        // success:function(json) {
        //     document.forms["post-form"].reset();
        //     document.getElementById("prediction").innerHTML = json['result']
        //     document.getElementById("Q1A").innerHTML = json['Q1A']
        //     document.getElementById("Q2A").innerHTML = json['Q2A']
        //     document.getElementById("Q3A").innerHTML = json['Q3A']
        //     document.getElementById("Q4A").innerHTML = json['Q4A']
        //     document.getElementById("Q5A").innerHTML = json['Q5A']
        //     document.getElementById("Q6A").innerHTML = json['Q6A']
        //     document.getElementById("Q7A").innerHTML = json['Q7A']
        //     document.getElementById("Q8A").innerHTML = json['Q8A']
        //     document.getElementById("Q9A").innerHTML = json['Q9A']
        //     document.getElementById("Q10A").innerHTML = json['Q10A']
        //     document.getElementById("Q11A").innerHTML = json['Q11A']
        //     document.getElementById("Q12A").innerHTML = json['Q12A']
        //     document.getElementById("Q13A").innerHTML = json['Q13A']
        //     document.getElementById("Q14A").innerHTML = json['Q14A']
        //     document.getElementById("Q15A").innerHTML = json['Q15A']
        //     document.getElementById("Q16A").innerHTML = json['Q16A']
        //     document.getElementById("Q17A").innerHTML = json['Q17A']
        //     document.getElementById("Q18A").innerHTML = json['Q18A']
        //     document.getElementById("Q19A").innerHTML = json['Q19A']
        //     document.getElementById("Q20A").innerHTML = json['Q20A']
        //     document.getElementById("Q21A").innerHTML = json['Q21A']
        //     document.getElementById("Q22A").innerHTML = json['Q22A']
        //     document.getElementById("Q23A").innerHTML = json['Q23A']
        //     document.getElementById("Q24A").innerHTML = json['Q24A']
        //     document.getElementById("Q25A").innerHTML = json['Q25A']
        //     document.getElementById("Q26A").innerHTML = json['Q26A']
        //     document.getElementById("Q27A").innerHTML = json['Q27A']
        //     document.getElementById("Q28A").innerHTML = json['Q28A']
        //     document.getElementById("Q29A").innerHTML = json['Q29A']
        //     document.getElementById("Q30A").innerHTML = json['Q30A']
        //     document.getElementById("Q31A").innerHTML = json['Q31A']
        //     document.getElementById("Q32A").innerHTML = json['Q32A']
        //     document.getElementById("Q33A").innerHTML = json['Q33A']
        //     document.getElementById("Q34A").innerHTML = json['Q34A']
        //     document.getElementById("Q35A").innerHTML = json['Q35A']
        //     document.getElementById("Q36A").innerHTML = json['Q36A']
        //     document.getElementById("Q37A").innerHTML = json['Q37A']
        //     document.getElementById("Q38A").innerHTML = json['Q38A']
        //     document.getElementById("Q39A").innerHTML = json['Q39A']
        //     document.getElementById("Q40A").innerHTML = json['Q40A']
        //     document.getElementById("Q41A").innerHTML = json['Q41A']
        //     document.getElementById("Q42A").innerHTML = json['Q42A']
    
        //     },
        //     error : function(xhr,errmsg,err) {

        // }

    })
})