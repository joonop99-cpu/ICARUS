# Finding Structure in Time__WIMQL7RR.pdf
# Source: /Users/joonoh/Desktop/OpenClaw_Library/papers/time-estimation/Finding Structure in Time__WIMQL7RR.pdf
# Pages extracted: 1-15 of 33


--- Page 1 ---
COGNITIVE SCIENCE 14, 179-21 1 (1 990) 
Finding Structure in Time 
JEFFREY L. ELMAN 
University of Calcfornia, San Riego 
Time underlies many interesting human behaviors. Thus, the question of how to 
represent time in connectionist models is very important. One approach is to rep- 
resent time implicitly by its effects on processing rather than explicitly (as in a 
spatial representation). The current report develops a proposal along these lines 
first described by Jordan (1986) which involves the use of recurrent links in order 
to provide networks with a dynamic memory. In this approach, hidden unit pat- 
terns are fed back to themselves: the internal representations which develop 
thus reflect task demands in the context of prior internal states. A set of simula- 
tions is reported which range from relatively simple problems (temporal version 
of XOR) to discovering syntactic/semantic features for words. The networks are 
able to learn interesting internal representations which incorporate task demands 
with memory demands: indeed, in this approach the notion of memory is inextri- 
cably bound up with task processing. These representations reveal a rich struc- 
ture, which allows them to be highly context-dependent, while also expressing 
generalizations across classes of items. These representations suggest a method 
for representing lexical categories and the type/token distinction. 
INTRODUCTION 
Time is clearly important in cognition. It is inextricably bound up with 
many behaviors (such as language) which express themselves as temporal 
sequences. Indeed, it is difficult to know how one might deal with such basic 
problems as goal-directed behavior, planning, or causation without some 
way of representing time. 
The question of how to represent time might seem to arise as a special 
problem unique to parallel-processing models, if only because the parallel 
nature of computation appears to be at odds with the serial nature of tem- 
I would like to thank Jay McClelland, Mike Jordan, Mary Hare, Dave Rumelhart, Mike 
Mozer, Steve Poteet, David Zipser, and Mark Dolson for many stimulating discussions. I thank 
McClelland, Jordan, and two anonymous reviewers for helpful critical comments on an earlier 
draft of this article. 
This work was supported by contract NOW1 14-85-K-0076 from the Office of Naval Re- 
search and contract DUB-07-87-C-H027 from Army Avionics, Ft. Monmouth. 
Correspondence and requests for reprints should be sent to Jeffrey L. Elman, Center for 
Research in Language, C-008, University of California, La Jolla, CA 92093. 
179 


--- Page 2 ---
180 
ELMAN 
poral events. However, even within traditional (serial) frameworks, the repre- 
sentation of serial order and the interaction of a serial input or output with 
higher levels of representation presents challenges. For example, in models 
of motor activity, an important issue is whether the action plan is a literal 
specification of the output sequence, or whether the plan represents serial 
order in a more abstract manner (e.g., Fowler, 1977,1980; Jordan & Rosen- 
baum, 1988; Kelso, Saltzman, & Tuller, 1986; Lashley, 1951; MacNeilage, 
1970; Saltzman & Kelso, 1987). Linguistic theoreticians have perhaps tended 
to be less concerned with the representation and processing of the temporal 
aspects to utterances (assuming, for instance, that all the information in an 
utterance is somehow made available simultaneously in a syntactic tree); but 
the research in natural language parsing suggests that the problem is not 
trivially solved (e.g., Frazier & Fodor, 1978; Marcus, 1980). Thus, what is 
one of the most elementary facts about much of human activity-that it has 
temporal extend-is 
sometimes ignored and is often problematic. 
In parallel distributed processing models, the processing of sequential 
inputs has been accomplished in several ways. The most common solution is 
to attempt to “paralielize time” by giving it a spatial representation. How- 
ever, there are problems with this approach, and it is ultimately not a good 
solution. A better approach would be to represent time implicitly rather 
than explicitly. That is, we represent time by the effect it has on processing 
and not as an additional dimension of the input. 
This article describes the results of pursuing this approach, with particu- 
lar emphasis on problems that are relevant to natural language processing. 
The approach taken is rather simple, but the results are sometimes complex 
and unexpected. Indeed, it seems that the solution to the problem of time 
may interact with other problems for connectionist architectures, including 
the problem of symbolic representation and how connectionist representa- 
tions encode structure. The current approach supports the notion outlined 
by Van Gelder (in press) (see also, Elman, 1989; Smolensky, 1987, 1988), 
that connectionist representations may have a functional compositionality 
without being syntactically compositional. 
The first section briefly describes some of the problems that arise when 
time is represented externally as a spatial dimension. The second section 
describes the approach used in this work. The major portion of this article 
presents the results of applying this new architecture to a diverse set of prob- 
lems. These problems range in complexity from a temporal version of the 
Exclusive-OR function to the discovery of syntactic/semantic categories in 
natural language data. 
THE PROBLEM WITH TIME 
One obvious way of dealing with patterns that have a temporal extent is to 
represent time explicitly by associating the serial order of the pattern with 
 15516709, 1990, 2, Downloaded from https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1402_1 by Seoul National University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 3 ---
FINDING STRUCTURE IN TIME 
181 
the dimensionality of the pattern vector. The first temporal event is repre- 
sented by the first element in the pattern vector, the second temporal event 
is represented by the second position in the pattern vector, and so on. The 
entire pattern vector is processed in parallel by the model. This approach 
has been used in a variety of models (e.g., Cottrell, Munro, & Zipser, 1987; 
Elman & Zipser, 1988; Hanson & Kegl, 1987). 
There are several drawbacks to this approach, which basically uses a 
spatial metaphor for time. First, it requires that there be some interface with 
the world, which buffers the input, so that it can be presented all at once. It 
is not clear that biological systems make use of such shift registers. There 
are also logical problems: How should a system know when a buffer’s con- 
tents should be examined? 
Second, the shift register imposes a rigid limit on the duration of patterns 
(since the input layer must provide for the longest possible pattern), and 
furthermore, suggests that all input vectors be the same length. These prob- 
lems are particularly troublesome in domains such as language, where one 
would like comparable representations for patterns that are of variable 
length. This is as true of the basic units of speech (phonetic segments) as it is 
of sentences. 
Finally, and most seriously, such an approach does not easily distinguish 
relative temporal position from absolute temporal position. For example, 
consider the following two vectors. 
[ 0 1 1 1 0 0 0 0 0 1  
[ 0 0 0 1 1 1 0 0 0 1  
These two vectors appear to be instances of the same basic pattern, but dis- 
placed in space (or time, if these are given a temporal interpretation). How- 
ever, as the geometric interpretation of these vectors makes clear, the two 
patterns are in fact quite dissimilar and spatially distant.’ PDP models can, 
of course, be trained to treat these two patterns as similar. But the similarity 
is a consequence of an external teacher and not of the similarity structure of 
the patterns themselves, and the desired similarity does not generalize to 
novel patterns. This shortcoming is serious if one is interested in patterns in 
which the relative temporal structure is preserved in the face of absolute 
temporal displacements. 
What one would like is a representation of time that is richer and does 
not have these problems. In what follows here, a simple architecture is 
described, which has a number of desirable temporal properties, and has 
yielded interesting results. 
I The reader may more easily be convinced of this by comparing the locations of the vectors 
11 0 01, [O 1 01, and 10 0 11 in 3-space. Although these patterns might be considered “temporally 
displaced” versions of the same basic pattern, the vectors are very different. 
 15516709, 1990, 2, Downloaded from https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1402_1 by Seoul National University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 4 ---
1 82 
ELMAN 
NETWORKS WITH MEMORY 
The spatial representation of time described above treats time as an explicit 
part of the input. There is another, very different possibility: Allow time to 
be represented by the effect it has on processing. This means giving the pro- 
cessing system dynamic properties that are responsive to temporal sequences. 
In short, the network must be given memory. 
There are many ways in which this can be accomplished, and a number 
of interesting proposals have appeared in the literature (e.g., Jordan, 1986; 
Pineda, 1988; Stornetta, Hogg, & Huberman, 1987; Tank & Hopfield, 1987; 
Waibel, Hanazawa, Hinton, Shikano, & Lang, 1987; Watrous & Shastri, 
1987; Williams & Zipser, 1988). One of the most promising was suggested 
by Jordan (1986). Jordan described a network (shown in Figure 1) contain- 
ing recurrent connections that were used to associate a static pattern (a 
“Plan”) with a serially ordered output pattern (a sequence of “Actions”). 
The recurrent connections allow the network’s hidden units to see its own 
previous output, so that the subsequent behavior can be shaped by previous 
responses. These recurrent connections are what give the network memory. 
This approach can be modified in the following way. Suppose a network 
(shown in Figure 2) is augmented at the input level by additional units; call 
these Context Units. These units are also “hidden” in the sense that they 
interact exclusively with other nodes internal to the network, and not the 
outside world. 
Imagine that there is a sequential input to be processed, and some clock 
which regulates presentation of the input to the network. Processing would 
then consist of the following sequence of events. At time t, the input units 
receive the first input in the sequence. Each unit might be a single scalar 
value or a vector, depending upon the nature of the problem. The context 
units are initially set to 0.5.* Both the input units and context units activate 
the hidden units; the hidden units then feed forward to activate the output 
units. The hidden units also feed back to activate the context units. This 
constitutes the forward activation. Depending upon- the task, there may or 
may not be a learning phase in this time cycle. If so, the output is compared 
with a teacher input, and back propagation of error (Rumelhart, Hinton, & 
Williams, 1986) is used to adjust connection strengths incrementally. Recur- 
rent connections are fixed at 1.0 and are not subject to adj~stment.~ 
At the 
next time step, t+ 1, the above sequence is repeated. This time the context 
The activation function used here bounds values between 0.0 and 1.0. 
’ A little more detail is in order about the connections between the context units and hidden 
units. In the networks used here, there were one-for-one connections between each hidden unit 
and each context unit. This implies that there are an equal number of context and hidden units. 
The upward connections between the context units and the hidden units were fully distributed, 
such that each context unit activates all the hidden units. 
 15516709, 1990, 2, Downloaded from https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1402_1 by Seoul National University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 5 ---
FINDING STRUCTURE IN TIME 
OUTPUT 
183 
INPUT 
Figure 1. Architecture used by Jordan (1986). Connections from output to state units are 
one-for-one, with a fixed weight of 1 .O Not all connections are shown. 
units contain values which are exactly the hidden unit values at time 1. These 
context units thus provide the network with memory. 
Internal Representation of Time. In feed forward networks employing 
hidden units and a learning algorithm, the hidden units develop internal 
representations for the input patterns that recode those patterns in a way 
which enables the network to produce the correct output for a given input. 
In the present architecture, the context units remember the previous internal 
state. Thus, the hidden units have the task of mapping both an external 
 15516709, 1990, 2, Downloaded from https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1402_1 by Seoul National University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 6 ---
184 
ELMAN 
OUTPUT UNITS 
, 
I , 
CONTEXT urws 
INPUT UNITS 
Figure 2. A simple recurrent network in which activations are copied from hidden layer to 
context layer on a one-for-one basis, with fixed weight of 1 .O. Dotted lines represent train- 
able connections. 
input, and also the previous internal state of some desired output. Because 
the patterns on the hidden units are saved as context, the hidden units must 
accomplish this mapping and at the same time develop representations which 
are useful encodings of the temporal properties of the sequential input. 
Thus, the internal representations that develop are sensitive to temporal 
context; the effect of time is implicit in these internal states. Note, however, 
that these representations of temporal context need not be literal. They rep- 
resent a memory which is highly task- and stimulus-dependent. 
 15516709, 1990, 2, Downloaded from https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1402_1 by Seoul National University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 7 ---
FINDING STRUCTURE IN TIME 
185 
Consider now the results of applying this architecture to a number of 
problems that involve processing of inputs which are naturally presented in 
sequence. 
EXCLUSIVE-OR 
The Exclusive-Or (XOR) function has been of interest because it cannot be 
learned by a simple two-layer network. Instead, it requires at least three 
layers. The XOR is usually presented as a problem involving 2-bit input 
vectors (00, 11, 01, 10) yielding 1-bit output vectors (0, 0, 1, 1, respectively). 
This problem can be translated into a temporal domain in several ways. 
One version involves constructing a sequence of 1 -bit inputs by presenting 
the 2-bit inputs one bit at a time (Le., in 2 time steps), followed by the 1-bit 
output; then continuing with another input/output pair chosen at random. 
A sample input might be: 
1 0  1 0 0 0 0 1  1 1  1 0  1 0 1 .  .. 
Here, the first and second bits are XOR-ed to produce the third; the fourth 
and fifth are XOR-ed to give the sixth; and so on. The inputs are concatenated 
and presented as an unbroken sequence. 
In the current version of the XOR problem, the input consisted of a 
sequence of 3,000 bits constructed in this manner. This input stream was 
presented to the network shown in Figure 2 (with 1 input unit, 2 hidden units, 
1 output unit, and 2 context units), one bit at a time. The task of the network 
was, at each point in time, to predict the next bit in the sequence. That is, 
given the input sequence shown, where one bit at a time is presented, the 
correct output at corresponding points in time is shown below. 
input: 
output: 
Recall that the actual input to the hidden layer consists of the input shown 
above, as well as a copy of the hidden unit activations from the previous 
cycle. The prediction is thus based not just on input from the world, but 
also on the network’s previous state (which is continuously passed back to 
itself on each cycle). 
Notice that, given the temporal structure of this sequence, it is only some- 
times possible to predict the next item correctly. When the network has 
received the first bit-1 in the example above-there is a 50% chance that 
the next bit will be a 1 (or a 0). When the network receives the second bit (0), 
however, it should then be possible to predict that the third will be the XOR, 
1. When the fourth bit is presented, the fifth is not predictable. But from 
the fifth bit, the sixth can be predicted, and so on. 
1 0  1 0  0 0 0 1 1  1 1  0 1.0 1. .. 
0 1 0  0 0  0 1 1  1 1  0 1 0  1 ?... 
- 
 15516709, 1990, 2, Downloaded from https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1402_1 by Seoul National University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 8 ---
186 
ELMAN 
0.50 c 
0.40 1 
0. 
Figure 3. Graph of root mean squared error over 12 consecutive inputs in sequential XOR 
task. Data points are averaged over 1200 trials. 
In fact, after 600 passes through a 3,000-bit sequence constructed in this 
way, the network's ability to predict the sequential input closely follows the 
above schedule. This can be seen by looking at the sum squared error in the 
output prediction at successive points in the input. The error signal provides 
a useful guide as to when the network recognized a temporal sequence, 
because at such moments its outputs exhibit low error. Figure 3 contains a 
plot of the sum squared error over 12 time steps (averaged over 1,200 cycles). 
The error drops at those points in the sequence where a correct prediction is 
possible; at other points; the error is high. This is an indication that the net- 
work has learned something about the temporal structure of the input, and 
is able to use previous context and current input to make predictions about 
future input. The network, in fact, attempts to use the XOR rule at'all points 
in time; this fact is obscured by the averaging of error, which is done for 
Figure 3. If one looks at the output activations, it is apparent from the nature 
of the errors that the network predicts successive inputs to be the XOR of 
the previous two. This is guaranteed to be successful every third bit, and will 
sometimes, fortuitously, also result in correct predictions at other times. 
It is interesting that the solution to the temporal version of XOR is some- 
what different than the static version of the same problem. In a network 
with two hidden units, one unit is highly activated when the input sequence 
is a series of identical elements (all 1s or Os), whereas the other unit is highly 
 15516709, 1990, 2, Downloaded from https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1402_1 by Seoul National University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 9 ---
FINDING STRUCTURE IN TIME 
187 
activated when the input elements alternate. Another way of viewing this is 
that the network develops units which are sensitive to high- and low-fre- 
quency inputs. This is a different solution than is found with feed-forward 
networks and simultaneously presented inputs. This suggests that problems 
may change their nature when cast in a temporal form. It is not clear that 
the solution will be easier or. more difficult in this form, but it is an impor- 
tant lesson to realize that the solution may be different. 
In this simulation, the prediction task has been used in a way that is 
somewhat analogous to auto-association. Auto-association is a useful tech- 
nique for discovering the intrinsic structure possessed by a set of patterns. 
This occurs because the network must transform the patterns into more 
compact representations; it generally does so by exploiting redundancies in 
the patterns. Finding these redundancies can be of interest because of what 
they reveal about the similarity structure of the data set (cf. Cottrell et al. 
1987; Elman & Zipser, 1988). 
In this simulation, the goal is to find the temporal structure of the XOR 
sequence. Simple auto-association would not work, since the task of simply 
reproducing the input at all points in time is trivially solvable and does not 
require sensitivity to sequential patterns. The prediction task is useful because 
its solution requires that the network be sensitive to temporal structure. 
STRUCTURE IN LETTER SEQUENCES 
One question which might be asked is whether the memory capacity of the 
network architecture employed here is sufficient to detect more complex 
sequential patterns than the XOR. The XOR pattern is simple in several 
respects. It involves single-bit inputs, requires a memory which extends only 
one bit back in time, and has only four different input patterns. More chal- 
lenging inputs would require multi-bit inputs of greater temporal extent, 
and a larger inventory of possible sequences. Variability in the duration of a 
pattern might also complicate the problem. 
An input sequence was devised which was intended to provide just these 
sorts of complications. The sequence was composed of six different 6-bit 
binary vectors. Although the vectors were not derived from real speech, one 
might think of them as representing speech sounds, with the six dimensions 
of the vector corresponding to articulatory features. Table 1 shows the vector 
for each of the six letters. 
The sequence was formed in two steps. First, the three consonants (b, d, 
g) were combined in random order to :btain a 1,000-letter sequence. Then, 
each consonant was replaced using the rules 
b- ba 
d- dii 
g- guuu 
 15516709, 1990, 2, Downloaded from https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1402_1 by Seoul National University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 10 ---
188 
ELMAN 
TABLE 1 
Vector Definitions of Alphabet 
Consonant 
Vowel 
Interrupted 
High 
Back 
Voiced 
b 
[
1
 
0 
1 
0 
0 
1
1
 
d 
1
1
 
0 
1 
1 
0 
1
1
 
g 
[
1
 
0 
1 
0 
1 
1
1
 
a 
[
O
 
1 
0 
0 
1 
1
1
 
I 
[
O
 
1 
0 
1 
0 
1
1
 
u 
[
O
 
1 
0 
1 
1 
1
1
 
Thus, an initial sequence of the form dbgbddg . . . gave rise to the final se- 
quence diibaguuubadiidiiguuu. . . (each letter being represented by one of 
the above 6-bit vectors). The sequence was semi-random; consonants occurred 
randomly, but following a given consonant, the identity and number of 
following vowels was regular. 
The basic network used in the XOR simulation was expanded to provide 
for the 6-bit input vectors; there were 6 input units, 20 hidden units, 6 out- 
put units, and 20 context units. 
The training regimen involved presenting each 6-bit input vector, one at a 
time, in sequence. The task for the network was to predict the next input. 
(The sequence wrapped around, that the first pattern was presented after 
the last.) The network was trained on 200 passes through the sequence. It 
was then tested on another sequence that obeyed the same regularities, but 
created from a different initial randomizaiton. 
The error signal for part of this testing phase is shown in Figure 4. Target 
outputs are shown in parenthesis, and the graph plots the corresponding 
error for each prediction. It is obvious that the error oscillates markedly; at 
some points in time, the prediction is correct (and error is low), while at 
other points in time, the ability to predict correctly is quite poor. More pre- 
cisely, error tends to be high when predicting consonants, and low when 
predicting vowels. 
Given the nature of the sequence, this behavior is sensible. The conso- 
nants were ordered randomly, but the vowels were not. Once the network 
has received a consonant as input, it can predict the identity of the following 
vowel. Indeed, it can do more; it knows how many tokens of the vowel to 
expect. At the end of the vowel sequence it has no way to predict the next 
consonant; at these points in time, the error is high. 
This global error pattern does not tell the whole story, however. Remem- 
ber that the input patterns (which are also the patterns the network is trying 
to predict) are bit vectors. The error shown in Figure 4 is the sum squared 
error over all 6 bits. Examine the error on a bit-by-bit basis; a graph of the 
error for bits [l] and [4] (over 20 time steps) is shown in Figure 5. There is a 
 15516709, 1990, 2, Downloaded from https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1402_1 by Seoul National University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 11 ---
FINDING STRUCTURE IN TIME 
189 
Figure 4. Graph of root mean squared error in letter prediction task. Labels indicate the 
correct output prediction at each point in time. Error is computed over the entire output 
vector. 
striking difference in the error patterns. Error on predicting the first bit is 
consistently lower than error for the fourth bit, and at all points in time. . 
Why should this be so? 
The first bit corresponds to the features Consonant; the fourth bit cor- 
responds to the feature High. It happens that while all consonants have the 
same value for the feature Consonant, they differ for High. The network 
has learned which vowels follow which consonants; this is why error on 
vowels is low. It has also learned how many vowels follow each consonant. 
An interesting corollary is that the network also knows how soon to expect 
the next consonant. The network cannot know which consonant, but it can 
predict correctly that a consonant follows. This is why the bit patterns for 
Consonant show low error, and the bit patterns for High show high error. 
(It is this behavior which requires the use of context units; a simple feed- 
forward network could learn the transitional probabilities from one input to 
the next, but could not learn patterns that span more than two inputs.) 
 15516709, 1990, 2, Downloaded from https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1402_1 by Seoul National University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 12 ---
Figure 5 (a). Graph of root mean squared error in letter prediction task. Error 
on bit 1, representing the feature CONSONANTAL. 
is computed 
Flgure 5 (b). Graph of root mean squared error in letter prediction task. Error is computed 
on bit 4, representing the feature HIGH. 
190 
 15516709, 1990, 2, Downloaded from https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1402_1 by Seoul National University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 13 ---
FINDING STRUCTURE IN TIME 
191 
This simulation demonstrates an interesting point. This input sequence 
was in some ways more complex than the XOR input. The serial patterns 
are longer in duration; they are of variable length so that a prediction de- 
pends upon a variable mount of temporal context; and each input consists 
of a 6-bit rather than a 1-bit vector. One might have reasonably thought 
that the more extended sequential dependencies of these patterns would 
exceed the temporal processing capacity of the network. But almost the 
opposite is true. The fact that there are subregularities (at the level of indi- 
vidual bit patterns) enables the network to make partial predictions, even in 
cases where the complete prediction is not possible. All of this is dependent 
upon the fact that the input is structured, of course. The lesson seems to be 
that more extended sequential dependencies may not necessarily be more 
difficult to learn. If the dependencies are structured, that structure may 
make learning easier and not harder. 
DISCOVERING THE NOTION “WORD” 
It is taken for granted that learning a language involves (among many other 
things) learning the sounds of that language, as well as the morphemes and 
words. Many theories of acquisition depend crucially upon such primitive 
types as word, or morpheme, or more abstract categories as noun, verb, or 
phrase (e.g., Berwick & Weinberg, 1984; Pinker, 1984). Rarely is it asked 
how a language learner knows when to begin or why these entities exist. 
These notions are often assumed to be innate. 
Yet, in fact, there is considerable debate among linguists and psycholin- 
guists about what representations are used in language. Although it is com- 
monplace to speak of basic units such as “phoneme,” “morpheme,” and 
“word,” these constructs have no clear and uncontroversial definition. 
Moreover, the commitment to such distinct levels of representation leaves a 
troubling residue of entities that appear to lie between the levels. For in- 
stance, in many languages, there are sound/meaning correspondences which 
lie between the phoneme and the morpheme (i.e., sound symbolism). Even 
the concept “word” is not as straightforward as one might think (cf. Green- 
berg, 1963; Lehman, 1962). In English, for instance, there is no consistently 
definable distinction among words (e.g., “apple”), compounds (“apple 
pie”) and phrases (“Library of Congress” or “man in the street”). Further- 
more, languages differ dramatically in what they treat as words. In polysyn- 
thetic languages (e.g., Eskimo), what would be called words more nearly 
resemble what the English speaker would call phrases or entire sentences. 
Thus, the most fundamental concepts of linguistic analysis have a fluidity, 
which at the very least, suggests an important role for learning; and the 
exact form of the those concepts remains an open and important question. 
In PDP networks, representational form and representational content 
often can be learned simultaneously. Moreover, the representations which 
1. 
 15516709, 1990, 2, Downloaded from https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1402_1 by Seoul National University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 14 ---
192 
ELMAN 
result have many of the flexible and graded characteristics noted above. 
Therefore, one can ask whether the notion “word” (or something which 
maps on to this concept) could emerge as a consequence of learning the 
sequential structure of letter sequences that form words and sentences (but 
in which word boundaries are not marked). 
Imagine then, another version of the previous task, in which the latter 
sequences form real words, and the words form sentences. The input will 
consist of the individual letters (imagine these as analogous to speech sounds, 
while recognizing that the orthographic input is vastly simpler than acoustic 
input would be). The letters will be presented in sequence, one at a time, 
with no breaks between the letters in a word, and no breaks between the 
words of different sentences. 
Such a sequence was created using a sentence-generating program and a 
lexicon of 15 words.4 The program generated 200 sentences of varying length, 
from four to nine words. The sentences were concatenated, forming a stream 
of 1,270 words. Next, the words were broken into their letter parts, yielding 
4,963 letters. Finally, each letter in each word was converted into a 5-bit 
random vector. 
The result was a stream of 4,963 separate 5-bit vectors, one for each 
letter. These vectors were the input and were presented one at a time. The 
task at each point in time was to predict the next letter. A fragment of the 
input and desired output is shown in Table 2. 
A network with 5 input units, 20 hidden units, 5 output units, and 20 
context units was trained on 10 complete presentations of the sequence. The 
error was relatively high at this point; the sequence was sufficiently random 
that it would be difficult to obtain very low error without memorizing the 
entire sequence (which would have required far more than 10 presentations). 
Nonetheless, a graph of error over time reveals an interesting pattern. A 
portion of the error is plotted in Figure 6; each data point is marked with 
the letter that should be predicted at that point in time. Notice that at the 
onset of each new word, the error is high. As more of the word is received 
the error declines, since the sequence is increasingly predictable. 
The error provides a good clue as to what the recurring sequences in the 
input are, and these correlate highly with words. The information is not 
categorical, however. The error reflects statistics of co-occurrence, and 
these are graded. Thus, while it is possible to determine, more or less, what 
sequences constitute words (those sequences bounded by high error), the 
criteria for boundaries are relative. This leads to ambiguities, as in the case 
of the y in they (see Figure 6); it could also lead to the misidentification of 
‘ The program used was a simplified version of the program described in greater detail in 
the next simulation. 
 15516709, 1990, 2, Downloaded from https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1402_1 by Seoul National University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


--- Page 15 ---
FINDING STRUCTURE IN TIME 
1 93 
TABLE 2 
Fragment of Training Sequence for letters-in-Words Simulation 
Input 
output 
01101 
(m) 
oooo1 
(0) 
00001 
(0) 
01110 (n) 
01110 (n) 
11001 
(Y) 
11001 
(Y) 
11001 
(Y) 
11001 
(Y) 
00101 (e) 
00101 
(e) 
oooo1 
(0) 
00001 
( 0 )  
10010 (r) 
10010 (r) 
10011 
( 5 )  
10011 
(s) 
oooO1 
(a) 
oooO1 (a) 
00111 
( 9 )  
00111 
( 9 )  
01111 
(0) 
01111 
( 0 )  
oooo1 
(0) 
00001 (a) 
oOo10 ( b )  
O0010 (b) 
01111 
(0) 
01111 
( 0 )  
11001 
(Y) 
11001 
(Y) 
oooO1 
(a) 
01110 (n) 
oooo1 
(0) 
01110 (n) 
00100 (d) 
00100 (d) 
00111 
( 9 )  
01001 (i) 
00111 
( 9 )  
01001 (i) 
10010 (r) 
10010 (r) 
01100 
( f )  
01100 ( I )  
01100 
( i )  
11001 
( i )  
common sequences that incorporate more than one word, but which co-occur 
frequently enough to be treated as a quasi-unit. This is the sort of behavior 
observed in children, who at early stages of language acquisition may treat 
idioms and other formulaic phrases as fixed lexical items (MacWhinney, 
1978). 
This simulation should -not be taken as a model of word acquisition. 
While listeners are clearly able to make predictions based upon partial input 
(Grosjean, 1980; Marslen-Wilson & Tyler, 1980; Salasoo & Pisoni, 1985), 
prediction is not the major goal of the language learner. Furthermore, the 
co-occurrence of sounds is only part of what identifies a word as such. The 
environment in which those sounds are uttered, and the linguistic context, 
are equally critical in establishing the coherence of the sound sequence and 
associating it with meaning. This simulation focuses only on a limited part 
of the information available to the language learner. The simulation makes 
the simple point that there is information in the signal that could serve as a 
cue to the boundaries of linguistic units which must be learned, and it demon- 
strates the ability of simple recurrent nerworks to extract this information. 
 15516709, 1990, 2, Downloaded from https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1402_1 by Seoul National University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
