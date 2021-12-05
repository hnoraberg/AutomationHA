

function myGSAutomationTask() {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  spreadsheet.insertSheet('Books, Authors and Ratings Spreadsheet');
  let values = spreadsheet.getRange("A1:C101").getValues();
  let form = FormApp.create("Questions About Top Rated Fiction Books from Goodreads");
  let item = form.addMultipleChoiceItem();
  item.setTitle("Please select your favourite author:");

  }
  item.setChoices(choices);
  MailApp.sendEmail('all_emails_accessed_from_spreadsheet_yet_to_be_created@mail.com',
  'Please fill this form', 'Please select your favourite author from the form: ' + form.getPublishedUrl());
}
