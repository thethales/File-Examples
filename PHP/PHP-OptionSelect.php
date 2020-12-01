<?php
$uf = 'SP';
?>

<label for="uf">UF</label>
<select class="form-control" type="text" value="<?php echo $UF?>" name="uf" id="uf" data-column="10">
  <option value=""></option>
  <option value="AC">Acre</option>
  <option value="SP" <?=$uf == 'SP' ? ' selected="selected"' : '';?> >São Paulo</option>
  
</select>