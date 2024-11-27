# SynthwaveAtomChallengeCreator

An atom is a very rough musical sketch of a track that is normally created within one hour. To get a starting point for
creating atoms as a regular practice, this small python script will create random instructions. The drums and chords
are tailored towards synthwave.

## Example Output

```
!atom

Tempo: 128 bpm
Timing: 4/4
Total length: 60-90s
Drums: Simmons SDSV
Key: D
Mode: mixolydian 
Notes in scale: [D, E, F#, G, A, B, C, D]
chord progression: [I, IV, VII, I] 
 I , DM , notes:  [D, F#, A]
 IV , GM , notes:  [G, B, D]
 VII , CM , notes:  [C, E, G]
 I , DM , notes:  [D, F#, A]
Modifiers: 
 Melody: Start on a non-chord tone
 Melody: Create an ascending melody
 Melody Pattern: Write a melody with the pattern A | A | A | B
```

There are parameters available to avoid randomizing specific parts, ask for them with any of the following command:

```
!atomhelp
```

E.g. full calls can look like this

```
!Atom --tempo 90 --drums 'Roland R8'
!atom --k C -m dorian
!Atom --chords 'I, vi7, IV, V7'
```
