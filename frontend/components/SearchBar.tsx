import * as React from 'react';
import InputAdornment from '@material-ui/core/InputAdornment';
import TextField from '@material-ui/core/TextField';
import SearchIcon from '@material-ui/icons/Search';

type SearchBarProps = {handleSearch: Function}
const SearchBar = ({handleSearch}: SearchBarProps) => {
  const [search, setSearch] = React.useState<string>('');

  const handleChange = (e) => {
    const searchQuery = e.target.value;
    setSearch(searchQuery)
    handleSearch(searchQuery);
  }
  return (
    <TextField
      value={search}
      onChange={handleChange}
      variant="filled"
      label="Search"
      fullWidth
      InputProps={{
        startAdornment: (
          <InputAdornment position="start">
            <SearchIcon />
          </InputAdornment>
        ),
      }}
    />
  );
};

export default SearchBar