<article class="markdown-body entry-content container-lg" itemprop="text"><h1><a id="user-content-explore-us-bikeshare-data" class="anchor" aria-hidden="true" href="#explore-us-bikeshare-data"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Explore-US-Bikeshare-Data</h1>
<p>Udacity Data Analyst Professional Track December 202</p>
<h2><a id="user-content-overview" class="anchor" aria-hidden="true" href="#overview"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Overview</h2>
<p>In this project, I will explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. Using Python, I will write a code import the data and answer interesting questions about it by computing <b>descriptive statistics</b>. I will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.</p>
<h2><a id="user-content-what-software-do-i-need" class="anchor" aria-hidden="true" href="#what-software-do-i-need"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>What Software Do I Need?</h2>
<p>To complete this project, i'll require the following softwares:</p>
<ul>
<li>Python</li>
<li>A text editor, like Sublime or Atom</li>
<li>A terminal application</li>
</ul>
<h2><a id="user-content-the-datasets" class="anchor" aria-hidden="true" href="#the-datasets"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>The Datasets</h2>
<p>The datasets provided by Motivate, a bike share system provider in the US, contains randomly selected data for the first six months of 2017 for all three cities. The data files for all three cities contain the same core six columns:</p>
<ul>
<li>Start Time</li>
<li>End Time</li>
<li>Trip Duration</li>
<li>Start Station</li>
<li>End Station</li>
<li>User Type</li>
</ul>
<p>The Chicago and New York City files also have the following two columns:</p>
<ul>
<li>Gender</li>
<li>Birth Year</li>
</ul>
<h2><a id="user-content-answering-questions" class="anchor" aria-hidden="true" href="#answering-questions"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Answering Questions</h2>
<p>Through writing code, I'm able to answer the following questions about the bike share data:</p>
<ul>
<li>What month occurs most often in the start time?</li>
<li>What day of the week (Monday, Tuesday, etc.) occurs most often in the start time?</li>
<li>What hour of the day occurs most often in the start time?</li>
<li>What is the total trip duration and average trip duration?</li>
<li>What is the most frequently used start station and most frequently used end station?</li>
<li>What is the most common trip (i.e., the combination of start station and end station that occurs the most often)?</li>
<li>What are the counts of each user type?</li>
<li>What are the counts of gender?</li>
<li>What is the earliest birth year (when the oldest person was born), most recent birth year, and most common birth year?</li>
</ul>
<p><a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/43564654/46038102-3f97f080-c11b-11e8-8417-c99f992afd86.png"><img src="https://user-images.githubusercontent.com/43564654/46038102-3f97f080-c11b-11e8-8417-c99f992afd86.png" alt="screen shot 2018-09-25 at 11 29 38 pm" style="max-width:100%;"></a></p>
<h2><a id="user-content-the-interactive-experience" class="anchor" aria-hidden="true" href="#the-interactive-experience"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>The Interactive Experience</h2>
<p>For a more interactive experience, I wrote a script that took raw input in the terminal to present the statistics. Below screenshots show the results after requesting for information in Chicago for the month of January on Sunday:</p>
<p><a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/43564654/46038089-36a71f00-c11b-11e8-9066-806aa9826f49.png"><img src="https://user-images.githubusercontent.com/43564654/46038089-36a71f00-c11b-11e8-9066-806aa9826f49.png" alt="screen shot 2018-09-25 at 11 27 59 pm" style="max-width:100%;"></a></p>
<p><a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/43564654/46038101-3eff5a00-c11b-11e8-97ff-4b96268545c4.png"><img src="https://user-images.githubusercontent.com/43564654/46038101-3eff5a00-c11b-11e8-97ff-4b96268545c4.png" alt="screen shot 2018-09-25 at 11 28 50 pm" style="max-width:100%;"></a></p>
</article>
