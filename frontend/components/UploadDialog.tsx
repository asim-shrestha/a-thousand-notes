import React, { useState } from "react";
import Button from "@material-ui/core/Button";
import DialogTitle from "@material-ui/core/DialogTitle";
import Dialog from "@material-ui/core/Dialog";
import { Box, DialogActions, DialogContent, DialogContentText, Input } from "@material-ui/core";
import TextField from "@material-ui/core/TextField";
import axios from "axios";
import { CircularProgress } from "@material-ui/core";



type UploadDialogProps = { loadImages: () => {}}
const UploadDialog = ({loadImages}: UploadDialogProps) => {
  const [open, setOpen] = useState(false);
  const [loading, setLoading] = useState(false);
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [imageName, setImageName] = useState<string>("");

  const handleClose = () => {
    setOpen(false);
    setImageName('');
    setSelectedFile(null);
  }

  const handleFinish = async () => {
    try {
      setLoading(true)
      let formData = new FormData();
      formData.append("files", selectedFile as any);
      await axios.post(
        `${process.env.NEXT_PUBLIC_API}/image/name/${imageName}`,
        formData,
        { headers: {"content-type": "multipart/form-data"}}
        );
    } catch (e) {
      alert(`Failed to upload image: ${e.message}`)
    } finally {
      loadImages();
      handleClose();
      setLoading(false);
    }
  }

  return (
    <div>
      {/* Dialog Open Button */}
      <Button
        size="large"
        variant="contained"
        onClick={() => setOpen(true)}
        color="primary"
      >
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
            onChange={(e: any) => setImageName(e.target.value)}
          />
          <Box mt={2} display="flex" flexDirection="row" justifyContent="center">
            <Button variant="contained" component="label" onChange={(e: any) => setSelectedFile(e.target.files[0])} color="primary">
              Upload
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
            disabled={loading}
          >
            Close
          </Button>
          <Button
            size="large"
            variant="contained"
            color="primary"
            onClick={handleFinish}
            disabled={loading || !imageName || !selectedFile}
          >
            <Box mr={1} mt={1} hidden={!loading}>
              <CircularProgress color="primary" size={20}/>
            </Box>
            Finish
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
};

export default UploadDialog;
