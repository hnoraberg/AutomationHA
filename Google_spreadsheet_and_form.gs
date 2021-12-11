
function myGSAutomationTask() {
  let spreadsheet = SpreadsheetApp.openByUrl('https://docs.google.com/spreadsheets/
  d/1KIUbwuk54H_CN9HU_sUmEdmkgw-QSTCQEtSOeqFYT-0/edit#gid=0')
  let values = spreadsheet.getRange("A2:A6").getValues();

  let form = FormApp.create("Questions About Top Rated Fiction Authors from Goodreads");
  let item = form.addMultipleChoiceItem();
  item.setTitle("Please select your favourite author:");
      .setChoices([
          item.createChoice(values.getRange(A2).getValue())
          item.createChoice(values.getRange(A3).getValue())
          item.createChoice(values.getRange(A4).getValue())
          item.createChoice(values.getRange(A5).getValue())
          item.createChoice(values.getRange(A6).getValue())
  }
  {
  let email_spreadsheet = SpreadsheetApp. openByUrl('https://docs.google.com/spreadsheets/
  d/1fujvRpjGsyEYoTnPqyZ1Ar1_zMkw46cEeJskUMEzme4/edit#gid=0'
  let email_values = spreadsheet.getRange().getValues
  MailApp.sendEmail(email_values,
  'Please fill this form', 'Please select your favourite author from the form: ' + form.getPublishedUrl());
}
