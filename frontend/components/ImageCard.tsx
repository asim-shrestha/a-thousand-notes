import * as React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import LinkIcon from '@material-ui/icons/Link';
import { Button } from '@material-ui/core';
import Typography from '@material-ui/core/Typography';
import ImageInfo from '../types/ImageInfo';
import ReactAudioPlayer from 'react-audio-player';
import { Checkbox } from '@material-ui/core';

const useStyles = makeStyles({
  root: {
    margin: '1.5em',
    maxWidth: 345,
  },
  linkButton: {
    borderRadius: "2em"
  }
});

type ImageCardProps = {
  imageInfo: ImageInfo
  checked: boolean,
  handleChecked: Function
}
const ImageCard = ({ imageInfo, checked, handleChecked }: ImageCardProps) => {
  const classes = useStyles();

  const openInSpotify = () => {
    location.href = imageInfo.spotify_uri;
  }

  return (
    <Card className={classes.root}>
      <CardActionArea>
        <CardMedia
          component="img"
          alt="Contemplative Reptile"
          height="120"
          image={imageInfo.image_url}
          title={imageInfo.image_name}
        />
        <CardContent onClick={() => handleChecked(imageInfo.id)}>
          <Typography gutterBottom variant="h5" component="h2">
            {imageInfo.image_name}
          </Typography>
          <Typography variant="body2" color="textSecondary">
            Linked to a spotify song called: "<b>{imageInfo.spotify_name}</b>".
          </Typography>
        </CardContent>
      </CardActionArea>
      <CardActions>
        <ReactAudioPlayer
          src={imageInfo.spotify_preview_url}
          controls
        />
        <Button
          className={classes.linkButton}
          variant="contained"
          color="primary"
          disableElevation
          onClick={openInSpotify}
        >
          <LinkIcon/>
        </Button>
        <Checkbox
          checked={checked}
          color="default"
          onClick={() => handleChecked(imageInfo.id)}
        />
      </CardActions>
    </Card>
  );
}

export default ImageCard