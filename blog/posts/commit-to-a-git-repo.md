## commit to the repo

Ok, you have now successfully cloned a Git-Repo. And now? Maybe let's establish some basic vocabularies first. When working with GIit, you can differentiate between the **working directory**, your **local Git-Repo** and some **remote Git-Repo**. 

### working directory

The working directory is the basically the directory (and all it's sub directories) you see in your file explorer. In this working directory you continue working as you did before you even heard of git. This means you can create files, move them around in all kind of sub directories, edit files, or even remove them. You can also rename files (which might cause some issues when you work on those files in other environments but usually you don't have to worry too much about renaming files).
Let's do some work.

* Open e.g. oXygen, create a new TEI document and save this file anywhere inside your **working directory** as `play.xml`. 
* Optionally create another file and save it somewhere else, maybe create a [markdown](https://en.wikipedia.org/wiki/Markdown) file, type some lines of text and save it as `markdownplay.xml`.

Your **working directory** could look now like on the screenshot below:

<img style="display:block; margin-left: auto; margin-right: auto; width:50%" src="https://acdh.oeaw.ac.at/redmine/projects/okopenko-diaries/repository/revisions/master/entry/img/6.jpg"/>

In a real work flow you would of course create some more valuable documents. And since those documents are that valuable, you would be very interested in methods of how to keep them save. (Otherwise you wouldn't probably read this). To keep your (newly created/modified) files save, you have to **commit** them to your (local/remote) Git-Repo. 

### local Git-Repo

Your local Git-Repo is part of your working directory. Depending on the settings of your file explorer, this local Git-Repo is displayed as a directory symbol named `.git` in your working directory. 

<img style="display:block; margin-left: auto; margin-right: auto; width:50%" src="https://acdh.oeaw.ac.at/redmine/projects/okopenko-diaries/repository/revisions/master/entry/img/7.jpg"/>

If you followed along so far and can't see anything like this, make sure you have **Hidden items** checked in your file explorers **View** settings.

<img style="display:block; margin-left: auto; margin-right: auto; width:50%" src="https://acdh.oeaw.ac.at/redmine/projects/okopenko-diaries/repository/revisions/master/entry/img/10.jpg"/>

You can double click on `.git` to explore your **local Git-Repo** but please don't change anything inside. 
What you should do instead is thinking about how to get your valuable (newly created/modified) documents **into this Repo/Directory**. To acchive this, you have to **commit your changes**. (actually you would have first to *add* those documents, but using the Tortoise-Client simplifies things a bit).
To commit changes

* go to your the root directory of your **working directory** and perform a **right mouse click**. 
* In the opened context menu you should see an option called **Git Commit -> "master"...**. 

<img style="display:block; margin-left: auto; margin-right: auto; width:50%" src="https://acdh.oeaw.ac.at/redmine/projects/okopenko-diaries/repository/revisions/master/entry/img/11.jpg"/>

* When you click on this option a new window opens.

<img style="display:block; margin-left: auto; margin-right: auto; width:50%" src="https://acdh.oeaw.ac.at/redmine/projects/okopenko-diaries/repository/revisions/master/entry/img/12.jpg"/>

The first thing you have to do there is to select all those files you actually want to **committed** to the repo. This means all those files you think they might be of some value. Continuing with our little play example, let's select `play.xml` and `markdownplay.md`. Since we created those files from scratch, they are listed by Tortoise under **Not Versioned Files**. As you can see on the screenshot, for my commit, Tortoise lists a "README.md" file under **Modified Fieles**. (This is the file which contains/contained the text you reading write now). This means that I committed this file in a former commit and now my Git-Repo always checks whenever I want to commit again, if this file (like all others I once committed) has been changed since the last commit.

* To proceed, check all files you want to (add and) commit. (Be aware of the **Check: All, None, ...** options.)
* Then write a **commit message**. 

### commit messages

The only formal constraint on the commit message is that it **must not be blank**. But it is strongly recommended to write some **useful** message. Messages which will give your future you (or anybody else) clues, what changes/progresses you introduced with this commit. To give an example: "Updated file xyz.xml" is NOT a usefull commit. "Transcribed pages 20-25 from Document XYZ and tagged all Persons" instead is a useful commit. 

* For our example we could write something like "added some sample data to get acquainted with GIT-commits". 

<img style="display:block; margin-left: auto; margin-right: auto; width:50%" src="https://acdh.oeaw.ac.at/redmine/projects/okopenko-diaries/repository/revisions/master/entry/img/13.jpg"/>

* After all valuable files are checked and the commit message is written, click on "Commit"
* This trigger the commit process which you can follow in a newly opend windows. This window summarizes the commit progress and when it's done gives you a summary of your commit. 

<img style="display:block; margin-left: auto; margin-right: auto; width:50%" src="https://acdh.oeaw.ac.at/redmine/projects/okopenko-diaries/repository/revisions/master/entry/img/14.jpg"/>

Congrats, you commited your files to you local Git-Repo.