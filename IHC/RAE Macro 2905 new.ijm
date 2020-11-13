roiManager("reset");

fn=getTitle();

output = getDirectory("Location for results");
//output=File.directory ;

run("Duplicate...", " ");
rename("temp")
//selectWindow("temp");
//run("RGB Color");
//selectWindow("temp");
//close();

setTool("polygon");
title="Draw Polygon";
msg="draw Polygon press t ";
waitForUser(title,msg);

roiManager("Deselect");
out = output + fn + " RoiSet.zip";
roiManager("Save", out);

selectWindow("temp");
run("Split Channels");
selectWindow("temp (green)");
close();
selectWindow("temp (red)");
close();
selectWindow("temp (blue)");

rename(fn);

setAutoThreshold("Default");

run("Threshold...");
title = "Get info";
msg = "set threshold\n and select OK to continue";
waitForUser(title, msg);


//run("Threshold...");
//setThreshold(0, 80);
setOption("BlackBackground", false);
run("Convert to Mask");
//



n=roiManager("count");

for (rois=0;rois<n;rois++){
roiManager("Select", rois);
a=Roi.getName;
rename(fn+" "+a);
run("Analyze Particles...", "size=0-infinity clear display summarize");

selectWindow("Results");
IJ.renameResults(fn+ " " + a + " results") ;
out = output + fn + " " + a + " Results";
saveAs("text", out);

//selectWindow("Results");

//saveAs("text");
}
selectWindow("Summary");
out = output +  fn  + " Summary";
saveAs("Results", out);

print ("done");

//IJ.renameResults(fn+" Summary") ;
//saveAs("Results");
//roiManager("Save", fn+".zip");







