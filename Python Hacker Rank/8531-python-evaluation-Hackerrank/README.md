# [Python Evaluation](https://www.hackerrank.com/challenges/python-eval/problem?isFullScreen=true)
## Easy
<div class="challenge-body-html"><div class="challenge_problem_statement"><div class="msB challenge_problem_statement_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>The <code>eval()</code> expression is a very powerful built-in function of Python. It helps in evaluating an expression. The expression can be a Python statement, or a code object.  </p>

<p>For example:  </p>

<div class="highlight"><pre><span></span><span class="o">&gt;&gt;&gt;</span> <span class="nb">eval</span><span class="p">(</span><span class="s2">"9 + 5"</span><span class="p">)</span>
<span class="mi">14</span>
<span class="o">&gt;&gt;&gt;</span> <span class="n">x</span> <span class="o">=</span> <span class="mi">2</span>
<span class="o">&gt;&gt;&gt;</span> <span class="nb">eval</span><span class="p">(</span><span class="s2">"x + 3"</span><span class="p">)</span>
<span class="mi">5</span>
</pre></div>


<p>Here, <code>eval()</code> can also be used to work with Python keywords or defined functions and variables. These would normally be stored as strings.  </p>

<p>For example:</p>

<div class="highlight"><pre><span></span><span class="o">&gt;&gt;&gt;</span> <span class="nb">type</span><span class="p">(</span><span class="nb">eval</span><span class="p">(</span><span class="s2">"len"</span><span class="p">))</span>
<span class="o">&lt;</span><span class="nb">type</span> <span class="s1">'builtin_function_or_method'</span><span class="o">&gt;</span>
</pre></div>


<p>Without eval()</p>

<div class="highlight"><pre><span></span><span class="o">&gt;&gt;&gt;</span> <span class="nb">type</span><span class="p">(</span><span class="s2">"len"</span><span class="p">)</span>
<span class="o">&lt;</span><span class="nb">type</span> <span class="s1">'str'</span><span class="o">&gt;</span>
</pre></div>


<p><strong>Task</strong> <br>
You are given an expression in a line. Read that line as a string variable, such as <em>var</em>, and print the result using <em>eval(var)</em>.  </p>

<p><strong>NOTE</strong>: Python2 users, please import <code>from __future__ import print_function</code>.  </p>

<p><strong>Constraint</strong> <br>
Input string is less than 100 characters.  </p>

<p><strong>Sample Input</strong>  </p>

<pre><code>print(2 + 3)
</code></pre>

<p><strong>Sample Output</strong>  </p>

<pre><code>5
</code></pre>

</div></div></div></div>