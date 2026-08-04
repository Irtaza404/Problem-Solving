# [HTML Parser - Part 1](https://www.hackerrank.com/challenges/html-parser-part-1/problem?isFullScreen=true)
## Easy
<div class="challenge-body-html"><div class="challenge_problem_statement"><div class="msB challenge_problem_statement_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p><strong><a href="https://www.google.co.in/webhp?sourceid=chrome-instant&amp;ion=1&amp;espv=2&amp;ie=UTF-8#q=What+is+HTML">HTML</a></strong> <br>
<em>Hypertext Markup Language</em> is a standard markup language used for creating World Wide Web pages.</p>

<p><strong><a href="https://en.wikipedia.org/wiki/Parsing">Parsing</a></strong> <br>
<em>Parsing</em> is the process of syntactic analysis of a string of symbols. It involves resolving a string into its component parts and describing their syntactic roles.</p>

<p><strong><a href="https://docs.python.org/3/library/html.parser.html">HTMLParser</a></strong> <br>
An <em>HTMLParser</em> instance is fed HTML data and calls handler methods when start tags, end tags, text, comments, and other markup elements are encountered. </p>

<p><strong>Example</strong> (from the Python 3 documentation):</p>

<p><strong><sub>Code</sub></strong></p>

<pre><code>from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()
parser.feed('&lt;html&gt;&lt;head&gt;&lt;title&gt;Test&lt;/title&gt;&lt;/head&gt;'
            '&lt;body&gt;&lt;h1&gt;Parse me!&lt;/h1&gt;&lt;/body&gt;&lt;/html&gt;')
</code></pre>

<p><strong><sub>Output</sub></strong></p>

<pre><code>Encountered a start tag: html
Encountered a start tag: head
Encountered a start tag: title
Encountered some data  : Test
Encountered an end tag : title
Encountered an end tag : head
Encountered a start tag: body
Encountered a start tag: h1
Encountered some data  : Parse me!
Encountered an end tag : h1
Encountered an end tag : body
Encountered an end tag : html  
</code></pre>

<p><a href="https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_starttag"><em>.handle_starttag(tag, attrs)</em></a>  </p>

<p>This method is called to handle the <em>start tag</em> of an element. (For example: &lt;div class='marks'&gt;) <br>
The <em>tag</em> argument is the name of the tag converted to lowercase. <br>
The <em>attrs</em> argument is a list of (name, value) pairs containing the attributes found inside the tag’s <em>&lt;&gt;</em> brackets.
<br><br></p>

<p><a href="https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_endtag"><em>.handle_endtag(tag)</em></a>  </p>

<p>This method is called to handle the <em>end tag</em> of an element. (For example: &lt;/div&gt;) <br>
The <em>tag</em> argument is the name of the tag converted to lowercase.
<br><br></p>

<p><a href="https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_startendtag"><em>.handle_startendtag(tag,attrs)</em></a> </p>

<p>This method is called to handle the <em>empty tag</em> of an element. (For example: &lt;br /&gt;) <br>
The <em>tag</em> argument is the name of the tag converted to lowercase. <br>
The <em>attrs</em> argument is a list of (name, value) pairs containing the attributes found inside the tag’s <em>&lt;&gt;</em> brackets.</p>

<hr>

<p><strong>Task</strong></p>

<p>You are given an <em>HTML</em> code snippet of <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)" data-darkreader-inline-stroke="" style="--darkreader-inline-stroke: currentColor;"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> lines. <br>
Your task is to print <em>start tags, end tags</em> and <em>empty tags</em> separately. </p>

<p>Format your results in the following way:</p>

<pre><code>Start : Tag1
End   : Tag1
Start : Tag2
-&gt; Attribute2[0] &gt; Attribute_value2[0]
-&gt; Attribute2[1] &gt; Attribute_value2[1]
-&gt; Attribute2[2] &gt; Attribute_value2[2]
Start : Tag3
-&gt; Attribute3[0] &gt; None
Empty : Tag4
-&gt; Attribute4[0] &gt; Attribute_value4[0]
End   : Tag3
End   : Tag2
</code></pre>

<p>Here, the <code>-&gt;</code> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value. <br>
The <code>&gt;</code> symbol acts as a separator of the attribute and the attribute value.</p>

<p>If an <em>HTML</em> tag has no attribute then simply print the name of the tag. <br>
If an attribute has no attribute value then simply print the name of the attribute value as <code>None</code>.  </p>

<p><strong>Note</strong>: Do not detect any <em>HTML</em> tag, attribute or attribute value inside the <em>HTML</em> comment tags (<code>&lt;!-- Comments --&gt;</code>).Comments can be multiline as well.<br></p></div></div></div><div class="challenge_input_format"><div class="msB challenge_input_format_title"><p><strong>Input Format</strong></p></div><div class="msB challenge_input_format_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>The first line contains integer <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)" data-darkreader-inline-stroke="" style="--darkreader-inline-stroke: currentColor;"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span>, the number of lines in a <em>HTML</em> code snippet.<br>
The next <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-2-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.064ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 888.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)" data-darkreader-inline-stroke="" style="--darkreader-inline-stroke: currentColor;"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g></svg></span> lines contain <em>HTML</em> code.</p></div></div></div><div class="challenge_constraints"><div class="msB challenge_constraints_title"><p><strong>Constraints</strong></p></div><div class="msB challenge_constraints_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><ul>
<li><span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="12.91ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 5558.6 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)" data-darkreader-inline-stroke="" style="--darkreader-inline-stroke: currentColor;"><path stroke-width="1" d="M96 585Q152 666 249 666Q297 666 345 640T423 548Q460 465 460 320Q460 165 417 83Q397 41 362 16T301 -15T250 -22Q224 -22 198 -16T137 16T82 83Q39 165 39 320Q39 494 96 585ZM321 597Q291 629 250 629Q208 629 178 597Q153 571 145 525T137 333Q137 175 145 125T181 46Q209 16 250 16Q290 16 318 46Q347 76 354 130T362 333Q362 478 354 524T321 597Z"></path><g transform="translate(778,0)"><path stroke-width="1" d="M694 -11T694 -19T688 -33T678 -40Q671 -40 524 29T234 166L90 235Q83 240 83 250Q83 261 91 266Q664 540 678 540Q681 540 687 534T694 519T687 505Q686 504 417 376L151 250L417 124Q686 -4 687 -5Q694 -11 694 -19Z"></path></g><g transform="translate(1834,0)"><path stroke-width="1" d="M234 637Q231 637 226 637Q201 637 196 638T191 649Q191 676 202 682Q204 683 299 683Q376 683 387 683T401 677Q612 181 616 168L670 381Q723 592 723 606Q723 633 659 637Q635 637 635 648Q635 650 637 660Q641 676 643 679T653 683Q656 683 684 682T767 680Q817 680 843 681T873 682Q888 682 888 672Q888 650 880 642Q878 637 858 637Q787 633 769 597L620 7Q618 0 599 0Q585 0 582 2Q579 5 453 305L326 604L261 344Q196 88 196 79Q201 46 268 46H278Q284 41 284 38T282 19Q278 6 272 0H259Q228 2 151 2Q123 2 100 2T63 2T46 1Q31 1 31 10Q31 14 34 26T39 40Q41 46 62 46Q130 49 150 85Q154 91 221 362L289 634Q287 635 234 637Z"></path></g><g transform="translate(3000,0)"><path stroke-width="1" d="M694 -11T694 -19T688 -33T678 -40Q671 -40 524 29T234 166L90 235Q83 240 83 250Q83 261 91 266Q664 540 678 540Q681 540 687 534T694 519T687 505Q686 504 417 376L151 250L417 124Q686 -4 687 -5Q694 -11 694 -19Z"></path></g><g transform="translate(4057,0)"><path stroke-width="1" d="M213 578L200 573Q186 568 160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302 660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46 152 46T177 47T193 50T201 52T207 57T213 61V578Z"></path><path stroke-width="1" d="M96 585Q152 666 249 666Q297 666 345 640T423 548Q460 465 460 320Q460 165 417 83Q397 41 362 16T301 -15T250 -22Q224 -22 198 -16T137 16T82 83Q39 165 39 320Q39 494 96 585ZM321 597Q291 629 250 629Q208 629 178 597Q153 571 145 525T137 333Q137 175 145 125T181 46Q209 16 250 16Q290 16 318 46Q347 76 354 130T362 333Q362 478 354 524T321 597Z" transform="translate(500,0)"></path><path stroke-width="1" d="M96 585Q152 666 249 666Q297 666 345 640T423 548Q460 465 460 320Q460 165 417 83Q397 41 362 16T301 -15T250 -22Q224 -22 198 -16T137 16T82 83Q39 165 39 320Q39 494 96 585ZM321 597Q291 629 250 629Q208 629 178 597Q153 571 145 525T137 333Q137 175 145 125T181 46Q209 16 250 16Q290 16 318 46Q347 76 354 130T362 333Q362 478 354 524T321 597Z" transform="translate(1001,0)"></path></g></g></svg></span></li>
</ul></div></div></div><div class="challenge_output_format"><div class="msB challenge_output_format_title"><p><strong>Output Format</strong></p></div><div class="msB challenge_output_format_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>Print the <em>HTML</em> tags, attributes and attribute values in order of their occurrence from top to bottom in the given snippet.<br></p>

<p>Use proper formatting as explained in the problem statement.</p></div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><pre><code>2
&lt;html&gt;&lt;head&gt;&lt;title&gt;HTML Parser - I&lt;/title&gt;&lt;/head&gt;
&lt;body data-modal-target class='1'&gt;&lt;h1&gt;HackerRank&lt;/h1&gt;&lt;br /&gt;&lt;/body&gt;&lt;/html&gt;
</code></pre></div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><pre><code>Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-&gt; data-modal-target &gt; None
-&gt; class &gt; 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html
</code></pre></div></div></div></div>