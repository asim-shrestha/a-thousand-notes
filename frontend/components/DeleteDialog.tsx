import React, { useState } from "react";
import Button from "@material-ui/core/Button";
import DialogTitle from "@material-ui/core/DialogTitle";
import Dialog from "@material-ui/core/Dialog";
import { Box, DialogActions, DialogContent, DialogContentText } from "@material-ui/core";
import axios from "axios";
import { CircularProgress } from "@material-ui/core";
import theme from "./theme";


type UploadDialogProps = { 
  selectedImageIds: string[],
  loadImages: () => {}
}
const UploadDialog = ({selectedImageIds, loadImages}: UploadDialogProps) => {
  const [open, setOpen] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleClose = () => {
    setOpen(false);
  }

  const handleFinish = async () => {
    try {
      setLoading(true)
      await axios.delete(
        `${process.env.NEXT_PUBLIC_API}/image/`,
        selectedImageIds
      );
    } catch (e) {
      alert(`Failed to delete image(s): ${e.message}`)
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
        style={{backgroundColor: selectedImageIds.length ? theme.palette.error.main : '', color: 'white'}}
        disabled={selectedImageIds.length < 1}
        >
        Delete
      </Button>

      {/* Dialog */}
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle id="simple-dialog-title">Delete image(s)</DialogTitle>
        <DialogContent dividers>
          <DialogContentText>
            Are you sure you would like to delete {selectedImageIds.length} selected images?
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button
            size="large"
            variant="contained"
            color="secondary"
            onClick={handleFinish}
            disabled={loading}
            >
            Yes
          </Button>
          <Button
            size="large"
            variant="contained"
            color="primary"
            onClick={() => setOpen(false)}
            disabled={loading}
          >
            <Box mr={1} mt={1} hidden={!loading}>
              <CircularProgress color="primary" size={20}/>
            </Box>
            No
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
};

export default UploadDialog;
