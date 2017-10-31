function correctMethodeName() {
    return "Output Message";
}

/*var result = wrongMethodeName(3);
document.writeln(result);*/

try {
    var result = wrongMethodeName(3);
    document.writeln(result);
}
catch (error) {
    document.writeln('<h3>Error:&nbsp;</h3><p>' + error +"</p>");
}