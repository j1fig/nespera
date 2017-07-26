nespera
=======

[![Join the chat at https://gitter.im/nespr/Lobby](https://badges.gitter.im/nespr/Lobby.svg)](https://gitter.im/nespr/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


### deployment cheatsheet

`ansible-playbook -i hosts/prod --private-key ../private/nespera.pem webservers.yml`



### Roadmap
- get a simple static page deployed
- Do a simple Python app deployment 
- Do a simple DB migration 
 - detect change on online news RSS/Atom feeds and display them clearly as printed press usually does.
    * this shows clearly click-bait-driven online media websites that change title/text on the fly to monetise on their content.
    * this crawls and stores feed resources in a (hopefully) efficient manner.
 - detect contradictory presentation on the same facts
    * this shows when a particular media source displays a title with a connotation that is negative when all the others display a positive one and vice-versa (this can be done with relatively simple NLP)

### Status
Trying to get the devops part done right first. 

After that will start on roadmap work
