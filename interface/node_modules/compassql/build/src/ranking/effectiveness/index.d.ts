import { SpecQueryModel } from '../../model';
import { Schema } from '../../schema';
import { QueryConfig } from '../../config';
import { RankingScore } from '../ranking';
export declare function effectiveness(specM: SpecQueryModel, schema: Schema, opt: QueryConfig): RankingScore;
