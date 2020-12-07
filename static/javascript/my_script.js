// console.log("Hello Initiative Tracker.")
//  Delete Character Modal
$('#deleteCharacterModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); // Button that triggered the modal
    var character_id = button.data('character_id'); // Extract info from data-* attributes
    console.log("character id is: " + character_id);
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    var modal = $(this);
    modal.find('#deleteCharacterForm').attr("action", "/initiative/character/" + character_id + "/destroy");
    })

//  Leave Campaign Modal
$('#leaveCampaignModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); // Button that triggered the modal
    var campaign_name = button.data('campaign_name');
    var campaign_id = button.data('campaign_id'); // Extract info from data-* attributes
    // console.log("campaign name is: " + campaign_name);
    // console.log("campaign id is: " + campaign_id);
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    var modal = $(this);
    modal.find('#campaign_to_leave_name').text(campaign_name)
    modal.find('#campaign_to_leave').attr("value", campaign_id);
    })

$('body').on('submit', '#initform', function(e){
    // console.log(this);
    e.preventDefault();
    // console.log($(this).serialize());
    // console.log("I stopped it!");
    $.ajax({
        url: "/initiative/enter_init/",
        method: "POST",
        data: $(this).serialize(),
        success: function(serverResponse){
            // console.log("yay!");
            // console.log(dict(serverResponse));
            $("#init_div").html(serverResponse);
        }
    })
})