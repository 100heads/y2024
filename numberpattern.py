import random, math, sys, copy, time

digitlist = ("0",'1',"2","3","4","5","6",'7',"8","9")
#seed = random.randint(1,1000); seed = 1234 #124 gets 20,13 #418 = 22,19 #796526 = 27,19 #551635744 = ,34 #178298238 = ,36 #139479470 = ,,38                         
seedoutputs = list()
seedoutputslen = 0
seedoutputsavg = 0
end = random.randint(200000,1000000);start = random.randint(end - 200000,end)
specseed = 41
seedrange = 1,100000
#seedrange = start,end
#seedrange = 1234
if type(seedrange) != type((1,2)):
  seedrange = (seedrange,seedrange)
  doprint = 1
else:
  doprint = 0
#834 = 31,r27 #4407 = 32,r31
#4613 = 44,r79
#2343 = 32,r144 #4613 = 38,r58 #773846977 = 45,r21
#NORMAL PATTERN: #1234567 = 25,r111134 #1234 = 30,r19 #557635744 = 42,r19 #4557635744 = 43,r19 #4557635744555555555555555555555,r111111111122222222258

#SEED RANGE AVERAGE AND OUTPUT LENGTH:   #(1,10):a11.4,h16,hs1[5]   #(1,100):a11.17,h20,hs2[79]   #(1,1000):a13.941,h30,hs6[145]   #(1,10000):a15.3085,h36,hs4[1333]   #(1,100000):a15.92911,h39,hs60[11366,81899]   #(1,1000000):a16.286854,h41,hs15[333344]   #(1,10000000):a17.0615067,h44,hs105[3333499],l1,ls94,sp(41)20756                  


outputext = seedrange[0]
thetime = time.time()
for i in range(seedrange[1] - seedrange[0] + 1):
  seed = seedrange[0] + i
  output = seed
  alloutputs = list()
  looping = True
  loopmax = 10000
  loopint = 0
  while looping:
    loopint += 1
    if loopint == 1:
      if doprint == 1:
        print(output)
      alloutputs.append(output)
    if output < 0:
      sign = "-"
      signval = -1
    else:
      sign = ""
      signval = 1
    addend = 0
    newoutput = list()
    outputlist = list()
    #intmulti = 1
    for digit in str(output):
      if digit in digitlist:
        outputlist.extend(digit)
        #outputlist.append(str(output)[whd])
        addend += int(digit)*signval
    
    for digit in range(len(outputlist)):
      if digit == 0:
        newoutput.append(sign)
      minoutput = min(outputlist)
      newoutput.append(minoutput)
      outputlist.remove(minoutput)
    output = int("".join(newoutput)) + addend
    #output = newoutput + addend
    #output = abs(output + addend)
    if output not in alloutputs:
      alloutputs.append(output)
      if doprint == 1:
        print(output)
    else:
      looping = False
      if doprint == 1:
        print("The seed",seed,"generated",len(alloutputs),"number(s) before \nrepeating a number: %d." % output)
      seedoutputs.append(len(alloutputs))
      seedoutputsavg += len(alloutputs)
      seedoutputslen += 1
    if loopint >= loopmax - 1:
      looping = False
      print("Loop terminated.")

print("The process took %f seconds.\n" % (time.time() - thetime))

seedoutputsavg = seedoutputsavg/seedoutputslen
if doprint == 0:
  print("The average output length of each seed in the seed range\n%s is %s.\n" % (str(seedrange),str(seedoutputsavg)))
  #print("\nMore data is loading (highest output length)...\n")
  highseeds = list()
  highestseed = max(seedoutputs)
  for it in range(len(seedoutputs)):
    if seedoutputs[it] == highestseed:
      highseeds.append(seedrange[0] + it)
  print("The highest output length in the seed range is %d with the\n%d seed(s) to have it being %s.\n" % (highestseed,len(highseeds),highseeds))
  lowseeds = list()
  lowestseed = min(seedoutputs)
  for it in range(len(seedoutputs)):
    if seedoutputs[it] == lowestseed:
      lowseeds.append(seedrange[0] + it)
  print("The lowest output length in the seed range is %d with the\n%d seed(s) to have it being %s." % (lowestseed,len(lowseeds),lowseeds))
  if specseed != 0:
    specseeds = list()
    for it in range(len(seedoutputs)):
      if seedoutputs[it] == specseed:
        specseeds.append(seedrange[0] + it)
    print("\nThe specified output length in the seed range is %d with the\n%d seed(s) to have it being %s." % (specseed,len(specseeds),specseeds))
  else:
    print("\nNo specified output length to search for.")

#print(time.time() - thetime)
#9.2 to 9.9 seconds
#7.367 to 8.54 or 8.77 seconds







