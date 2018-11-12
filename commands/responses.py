from random import randint

introductions = ["I am listening",
	"What can I do for you?",
	"How can I help you?",
	"What do you need?",
	"How can I assist you today?"]

notFound = ["That query failed for some reason.",
	"Im not sure why, but that query seemed to fail.",
	"Query failed. Try again?",
	"I'm afraid I couldn't handle those inputs."]

wolframResult = ["Here is what I found boss:",
	"Here is what we are looking at:",
	"I found something:",
	"I found this:",
	"Here is what I have got"]

kanbanEvent = ["Ive added it to your kanban and marked it as an event",
	"Its been added as an event to your kanban",
	"Got it. Its on your kanban",
	"Got it. I put it in your events kanban",
	"Handled. I marked it as an event.",
	"I marked it as an event in your kanban.",
	"Its done. Its in your kanban under events."]

kanbanMeeting = ["Alright, your meeting is viewable from your kanban",
	"Ive put it on your meeting board",
	"I marked it as a meeting and added it to your workflow",
	"Ive integrated it into your existing workflow",
	"Got it. Its on your meetings kanban",
	"Alright. It's up. Check your meetings kanban when you get a chance.",
	"Handled. I marked it as a meeting. Its in your workflow"]

kanbanAssignment = ["Its in your kanban as an assignment",
	"Its in the assignments section of your kanban",
	"This looks important. You should get to work on it soon. Ive uploaded it to your kanban",
	"Ive put it on your assignments kanban.",
	"Its on your kanban. I marked it as an assignment."]

jokes = [

"Telling my daughter garlic is good for you. Good immune system and keeps pests away including ticks, mosquitos, vampires and men.",
"Ive been going through a really rough period at work this week. Its my own fault for swapping my tampax for sand paper.",
"If I could have dinner with anyone, dead or alive... ...I would choose alive. B.J. Novak",
"Two guys walk into a bar. The third guy ducks.",
"Why cant Barbie get pregnant? Because Ken comes in a different box. Heyowowowowowooooooo",
"Did you hear about the guy who blew his entire lottery winnings on a limousine? He had nothing left to chauffeur it.",
"What should you do before criticizing PacMan? WAKA WAKA WAKA mile in his shoes",
"What do you call a barbarian you cant see? an Invisigoth.",
"You ever notice that the most dangerous thing about marijuana is getting caught with it?",
"What does Miley Cyrus eat for Thanksgiving? Twerky! Just kidding... Drugs. She eats drugs.",
"My son just got a tattoo of a heart, a spade, a club, and a diamond, all without my permission. I guess Ill deal with him later.",
"What do you call a potato in space? Spudnik",
"What happens to a necrophiliac after death? Reserection",
"Why did the chicken hold a seance? To get to the other side.",
"Where do baby cows go to eat lunch? The calf-eteria.",
"Whats the difference between a painting and Jesus. You only require one nail to put up the painting.",
"I am looking forward to 6pm Thanksgiving Day when Walmart opens its doors for its annual sale of trampled human corpses.",
"Yttrium-barium-copper oxide walks into a bar and The bartender tells him, quote We don't serve superconductors here endquote. He leaves without resistance.",
"Every night, I take all of the singles out of my wallet, spread them on the bed, and pretend I was pretty that day.",
"Which gospel contains Jesus parable about the shades of numbers? (hard pause) Math hue.",
"Ibuprofen is my favorite headache medicine that also sounds like a reggae professor.",
"Ted Cruz getting elected.",
"Before I destroy a wasps nest I like to capture a single wasp and tell it my entire diabolical plan.",
"With Facebook, you can stay in touch with people you would otherwise never talk to, but that's only one of the many awful things about it"

]

def handle(samples):
	choice = randint(0,len(samples)-1)
	return samples[choice]

