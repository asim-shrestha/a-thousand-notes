import React, { useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import Button from "@material-ui/core/Button";
import DialogTitle from "@material-ui/core/DialogTitle";
import Dialog from "@material-ui/core/Dialog";
import { blue } from "@material-ui/core/colors";
import { Box, DialogActions, DialogContent, DialogContentText, Input } from "@material-ui/core";
import TextField from "@material-ui/core/TextField";

const useStyles = makeStyles({
  avatar: {
    backgroundColor: blue[100],
    color: blue[600],
  },
});

const UploadDialog = () => {
  const classes = useStyles();
  const [open, setOpen] = useState(false);
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [imageName, setImageName] = useState<string>("");

  const handleClose = () => {
    setOpen(false);
    setImageName('');
    setSelectedFile(null);
  }

  const handleFinish = () => {
    
  }

  return (
    <div>
      {/* Dialog Open Button */}
      <Button size="large" variant="contained" onClick={() => setOpen(true)}>
        Upload
      </Button>

      {/* Dialog */}
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle id="simple-dialog-title">Upload a new image</DialogTitle>
        <DialogContent dividers>
          <DialogContentText>
            Upload a new image onto our server!
            The image will automatically be linked to a related random song!  
          </DialogContentText>
          <TextField
            label="Image name"
            variant="filled"
            InputLabelProps={{
              shrink: true,
            }}
            fullWidth
            value={imageName}
            onChange={(e) => setImageName(e.target.value)}
          />
          <Box mt={2} display="flex" flexDirection="row" justifyContent="center">
            <Button variant="contained" component="label" onChange={e => setSelectedFile(e.target.files[0])}>
              Upload File
              <input type="file" hidden />
            </Button>
            <Box ml={2}>
              <Input value={selectedFile?.name || "File Name"} disabled/>
            </Box>
          </Box>
        </DialogContent>
        <DialogActions>
          <Button
            size="large"
            variant="contained"
            color="secondary"
            onClick={() => setOpen(false)}
          >
            Close
          </Button>
          <Button
            size="large"
            variant="contained"
            onClick={() => setOpen(false)}
            disabled={!imageName || !selectedFile}
          >
            Finish
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
};

export default UploadDialog;
